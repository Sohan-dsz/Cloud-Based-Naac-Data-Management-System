from django.db import models
from django.conf import settings
from apps.authentication.models import User


class Criteria(models.Model):
    """NAAC Criteria model (7 criteria)."""
    CRITERIA_CHOICES = [
        ('curricular_aspects', 'Curricular Aspects'),
        ('teaching_learning_evaluation', 'Teaching-Learning and Evaluation'),
        ('research_innovations_extension', 'Research, Innovations and Extension'),
        ('infrastructure_learning_resources', 'Infrastructure and Learning Resources'),
        ('student_support_learning', 'Student Support and Learning'),
        ('governance_leadership_management', 'Governance, Leadership and Management'),
        ('institutional_values_best_practices', 'Institutional Values and Best Practices'),
    ]

    name = models.CharField(max_length=50, choices=CRITERIA_CHOICES, unique=True)
    description = models.TextField(blank=True)
    weightage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return self.get_name_display()

    class Meta:
        verbose_name = 'Criteria'
        verbose_name_plural = 'Criteria'


class Evidence(models.Model):
    """Evidence model linking documents to criteria."""
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    criteria = models.ForeignKey(Criteria, on_delete=models.CASCADE, related_name='evidences')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Evidence'
        verbose_name_plural = 'Evidences'


class Document(models.Model):
    """Document model for uploaded files."""
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file_path = models.CharField(max_length=500)  # MinIO object key
    file_size = models.PositiveBigIntegerField()
    mime_type = models.CharField(max_length=100)
    evidence = models.ForeignKey(Evidence, on_delete=models.CASCADE, related_name='documents')
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    version = models.PositiveIntegerField(default=1)
    ocr_text = models.TextField(blank=True)  # Extracted text from OCR
    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_documents')
    approved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} (v{self.version})"

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
        ordering = ['-uploaded_at']
