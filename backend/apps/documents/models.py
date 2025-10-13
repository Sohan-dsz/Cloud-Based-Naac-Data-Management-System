from django.db import models
from django.contrib.auth import get_user_model
from simple_history.models import HistoricalRecords
import uuid

User = get_user_model()

class NAACCriteria(models.Model):
    """NAAC Criteria categories"""
    
    CRITERIA_CHOICES = [
        ('C1', 'Curricular Aspects'),
        ('C2', 'Teaching-Learning and Evaluation'),
        ('C3', 'Research, Innovations and Extension'),
        ('C4', 'Infrastructure and Learning Resources'),
        ('C5', 'Student Support and Progression'),
        ('C6', 'Governance, Leadership and Management'),
        ('C7', 'Institutional Values and Best Practices'),
    ]
    
    code = models.CharField(max_length=5, choices=CRITERIA_CHOICES, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    weightage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'naac_criteria'
        verbose_name = 'NAAC Criteria'
        verbose_name_plural = 'NAAC Criteria'
        ordering = ['code']
    
    def __str__(self):
        return f"{self.code}: {self.title}"


class DocumentCategory(models.Model):
    """Categories for organizing documents"""
    
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    naac_criteria = models.ForeignKey(NAACCriteria, on_delete=models.CASCADE, related_name='categories')
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    # History tracking
    history = HistoricalRecords()
    
    class Meta:
        db_table = 'document_categories'
        verbose_name = 'Document Category'
        verbose_name_plural = 'Document Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    @property
    def full_path(self):
        """Return full category path"""
        if self.parent_category:
            return f"{self.parent_category.full_path} > {self.name}"
        return self.name


class Document(models.Model):
    """Main document model"""
    
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('pending_review', 'Pending Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('archived', 'Archived'),
    ]
    
    # Basic information
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey(DocumentCategory, on_delete=models.CASCADE, related_name='documents')
    
    # File information
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=500)  # MinIO path
    file_size = models.BigIntegerField()  # Size in bytes
    file_type = models.CharField(max_length=10)  # PDF, DOC, JPG, etc.
    mime_type = models.CharField(max_length=100)
    
    # Content extraction
    extracted_text = models.TextField(blank=True)  # OCR text
    is_text_extracted = models.BooleanField(default=False)
    
    # Status and workflow
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_documents')
    reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviewed_documents')
    review_notes = models.TextField(blank=True)
    
    # Versioning
    version = models.CharField(max_length=10, default='1.0')
    parent_document = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='versions')
    is_current_version = models.BooleanField(default=True)
    
    # Tags and metadata
    tags = models.JSONField(default=list, blank=True)
    metadata = models.JSONField(default=dict, blank=True)
    
    # Academic year and period
    academic_year = models.CharField(max_length=9, blank=True)  # e.g., "2023-2024"
    document_date = models.DateField(null=True, blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)
    
    # History tracking
    history = HistoricalRecords()
    
    class Meta:
        db_table = 'documents'
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['category']),
            models.Index(fields=['uploaded_by']),
            models.Index(fields=['academic_year']),
            models.Index(fields=['created_at']),
        ]
    
    def __str__(self):
        return self.title
    
    @property
    def file_size_human(self):
        """Return human readable file size"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if self.file_size < 1024.0:
                return f"{self.file_size:.1f} {unit}"
            self.file_size /= 1024.0
        return f"{self.file_size:.1f} TB"
    
    def get_download_url(self):
        """Generate download URL"""
        # Implementation would depend on MinIO setup
        return f"/api/v1/documents/{self.id}/download/"


class DocumentComment(models.Model):
    """Comments on documents for review process"""
    
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'document_comments'
        verbose_name = 'Document Comment'
        verbose_name_plural = 'Document Comments'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Comment by {self.author.get_full_name()} on {self.document.title}"


class DocumentAccess(models.Model):
    """Track document access for audit purposes"""
    
    ACCESS_TYPES = [
        ('view', 'View'),
        ('download', 'Download'),
        ('edit', 'Edit'),
        ('delete', 'Delete'),
    ]
    
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='access_logs')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    access_type = models.CharField(max_length=10, choices=ACCESS_TYPES)
    ip_address = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=500, blank=True)
    
    # Timestamps
    accessed_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'document_access_logs'
        verbose_name = 'Document Access Log'
        verbose_name_plural = 'Document Access Logs'
        ordering = ['-accessed_at']
        indexes = [
            models.Index(fields=['document', 'accessed_at']),
            models.Index(fields=['user', 'accessed_at']),
        ]
    
    def __str__(self):
        return f"{self.user.username} {self.access_type} {self.document.title}"