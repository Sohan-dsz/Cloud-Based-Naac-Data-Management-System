from rest_framework import serializers
from .models import AuditLog


class AuditLogSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = AuditLog
        fields = ['id', 'user', 'action', 'resource_type', 'resource_id', 'details', 'ip_address', 'user_agent', 'timestamp']
        read_only_fields = ['id', 'user', 'timestamp']
