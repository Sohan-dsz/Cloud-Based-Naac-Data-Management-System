from rest_framework import serializers
from datetime import datetime

from django.contrib.auth import get_user_model
from .models import Task
from apps.documents.models import Criteria
from apps.documents.serializers import CriteriaSerializer
from apps.authentication.models import User

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'roles']

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)
    assigned_to_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='assigned_to', write_only=True, required=False
    )
    created_by = UserSerializer(read_only=True)
    related_criteria = CriteriaSerializer(read_only=True)
    related_criteria_id = serializers.PrimaryKeyRelatedField(
        queryset=Criteria.objects.all(), source='related_criteria', write_only=True, required=False
    )

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'status', 'priority', 'due_date',
            'assigned_to', 'assigned_to_id', 'created_by', 'related_criteria',
            'related_criteria_id', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_by', 'created_at', 'updated_at']

    def validate_due_date(self, value):
        if value < datetime.now().date():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value

    def validate_assigned_to_id(self, value):
        if value:
            request = self.context.get('request')
            if request and request.user.roles.filter(name__in=['iqac_admin', 'dept_admin']).exists():
                return value
            raise serializers.ValidationError("Only IQAC or Department admins can assign tasks.")
        return value
