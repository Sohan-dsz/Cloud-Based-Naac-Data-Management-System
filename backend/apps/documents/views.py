from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from minio import Minio
from meilisearch import Client as MeiliClient
import pytesseract
from PIL import Image
import io
from .models import Criteria, Evidence, Document
from .serializers import CriteriaSerializer, EvidenceSerializer, DocumentSerializer, DocumentUploadSerializer
from apps.audit.models import AuditLog


class CriteriaListView(generics.ListAPIView):
    queryset = Criteria.objects.all()
    serializer_class = CriteriaSerializer
    permission_classes = [IsAuthenticated]


class EvidenceListCreateView(generics.ListCreateAPIView):
    serializer_class = EvidenceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Evidence.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class EvidenceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EvidenceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Evidence.objects.filter(created_by=self.request.user)


class DocumentListView(generics.ListAPIView):
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Document.objects.all()
        evidence_id = self.request.query_params.get('evidence_id')
        if evidence_id:
            queryset = queryset.filter(evidence_id=evidence_id)
        return queryset


class DocumentUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = DocumentUploadSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data['file']
            evidence = Evidence.objects.get(id=serializer.validated_data['evidence_id'])

            # Upload to MinIO
            minio_client = Minio(
                settings.MINIO_ENDPOINT,
                access_key=settings.MINIO_ACCESS_KEY,
                secret_key=settings.MINIO_SECRET_KEY,
                secure=settings.MINIO_SECURE
            )

            if not minio_client.bucket_exists(settings.MINIO_BUCKET_NAME):
                minio_client.make_bucket(settings.MINIO_BUCKET_NAME)

            file_path = f"{evidence.criteria.name}/{evidence.id}/{file.name}"
            minio_client.put_object(
                settings.MINIO_BUCKET_NAME,
                file_path,
                file,
                file.size,
                content_type=file.content_type
            )

            # OCR processing
            ocr_text = ""
            if file.content_type in ['application/pdf', 'image/jpeg', 'image/png']:
                # For simplicity, assume image; in real app, handle PDF
                image = Image.open(file)
                ocr_text = pytesseract.image_to_string(image)

            # Create document
            document = Document.objects.create(
                title=serializer.validated_data['title'],
                description=serializer.validated_data.get('description', ''),
                file_path=file_path,
                file_size=file.size,
                mime_type=file.content_type,
                evidence=evidence,
                uploaded_by=request.user,
                ocr_text=ocr_text
            )

            # Index in Meilisearch
            meili_client = MeiliClient(settings.MEILISEARCH_URL, settings.MEILISEARCH_MASTER_KEY)
            meili_client.index('documents').add_documents([{
                'id': document.id,
                'title': document.title,
                'description': document.description,
                'ocr_text': ocr_text,
                'evidence_id': evidence.id,
                'criteria': evidence.criteria.name
            }])

            # Audit log
            AuditLog.objects.create(
                user=request.user,
                action='upload',
                resource_type='Document',
                resource_id=document.id,
                details=f"Uploaded document: {document.title}"
            )

            return Response(DocumentSerializer(document).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocumentSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.query_params.get('q', '')
        if not query:
            return Response({'error': 'Query parameter required'}, status=status.HTTP_400_BAD_REQUEST)

        meili_client = MeiliClient(settings.MEILISEARCH_URL, settings.MEILISEARCH_MASTER_KEY)
        results = meili_client.index('documents').search(query)

        document_ids = [hit['id'] for hit in results['hits']]
        documents = Document.objects.filter(id__in=document_ids)
        serializer = DocumentSerializer(documents, many=True)

        # Audit log
        AuditLog.objects.create(
            user=request.user,
            action='search',
            resource_type='Document',
            resource_id=0,  # No specific resource
            details=f"Searched for: {query}"
        )

        return Response(serializer.data)


class DocumentApproveView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            document = Document.objects.get(id=pk)
            document.is_approved = True
            document.approved_by = request.user
            document.save()

            # Audit log
            AuditLog.objects.create(
                user=request.user,
                action='approve',
                resource_type='Document',
                resource_id=document.id,
                details=f"Approved document: {document.title}"
            )

            return Response({'message': 'Document approved'})
        except Document.DoesNotExist:
            return Response({'error': 'Document not found'}, status=status.HTTP_404_NOT_FOUND)
