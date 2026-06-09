from django.urls import path
from .views import (
    CriteriaListView, EvidenceListCreateView, EvidenceDetailView,
    DocumentListView, DocumentUploadView, DocumentSearchView, DocumentApproveView
)

app_name = 'documents'

urlpatterns = [
    path('criteria/', CriteriaListView.as_view(), name='criteria-list'),
    path('evidence/', EvidenceListCreateView.as_view(), name='evidence-list-create'),
    path('evidence/<int:pk>/', EvidenceDetailView.as_view(), name='evidence-detail'),
    path('documents/', DocumentListView.as_view(), name='document-list'),
    path('documents/upload/', DocumentUploadView.as_view(), name='document-upload'),
    path('documents/search/', DocumentSearchView.as_view(), name='document-search'),
    path('documents/<int:pk>/approve/', DocumentApproveView.as_view(), name='document-approve'),
]
