from rest_framework import serializers
from .models import Criteria, Evidence, Document


class CriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criteria
        fields = ['id', 'name', 'description', 'weightage']


class EvidenceSerializer(serializers.ModelSerializer):
    criteria = CriteriaSerializer(read_only=True)
    criteria_id = serializers.IntegerField(write_only=True)
    document_count = serializers.SerializerMethodField()

    class Meta:
        model = Evidence
        fields = ['id', 'title', 'description', 'criteria', 'criteria_id', 'created_by', 'created_at', 'updated_at', 'document_count']
        read_only_fields = ['created_by', 'created_at', 'updated_at']

    def get_document_count(self, obj):
        return obj.documents.count()


class DocumentSerializer(serializers.ModelSerializer):
    evidence = EvidenceSerializer(read_only=True)
    evidence_id = serializers.IntegerField(write_only=True)
    uploaded_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Document
        fields = ['id', 'title', 'description', 'file_path', 'file_size', 'mime_type', 'evidence', 'evidence_id', 'uploaded_by', 'uploaded_at', 'version', 'ocr_text', 'is_approved', 'approved_by', 'approved_at']
        read_only_fields = ['uploaded_by', 'uploaded_at', 'approved_by', 'approved_at']


class DocumentUploadSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False)
    evidence_id = serializers.IntegerField()
    file = serializers.FileField()

    def validate_evidence_id(self, value):
        try:
            Evidence.objects.get(id=value)
        except Evidence.DoesNotExist:
            raise serializers.ValidationError("Evidence does not exist.")
        return value
