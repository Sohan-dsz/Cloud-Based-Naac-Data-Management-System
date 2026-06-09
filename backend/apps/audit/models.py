from django.db import models
from django.conf import settings


class AuditLog(models.Model):
    """Audit log model to track user actions."""
    ACTION_CHOICES = [
        ('upload', 'Document Upload'),
        ('approve', 'Document Approval'),
        ('delete', 'Document Delete'),
        ('report_generate', 'Report Generation'),
        ('search', 'Document Search'),
        ('access', 'Resource Access'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    resource_type = models.CharField(max_length=50)  # e.g., 'Document', 'Report'
    resource_id = models.PositiveIntegerField()
    details = models.TextField(blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_action_display()} - {self.timestamp}"

    class Meta:
        verbose_name = 'Audit Log'
        verbose_name_plural = 'Audit Logs'
        ordering = ['-timestamp']
