from rest_framework import generics, permissions
from rest_framework.response import Response
from django.db.models import Q

from .models import Task
from .serializers import TaskSerializer

class IsAdminOrAssigned(permissions.BasePermission):
    """
    Custom permission to allow only admins to create/assign tasks,
    and users to view/edit their own assigned tasks.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.roles.filter(name__in=['iqac_admin', 'dept_admin']).exists()

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj.assigned_to == request.user or obj.created_by == request.user
        return request.user.roles.filter(name__in=['iqac_admin', 'dept_admin']).exists() or obj.assigned_to == request.user

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrAssigned]

    def get_queryset(self):
        user = self.request.user
        if user.roles.filter(name__in=['iqac_admin', 'dept_admin']).exists():
            return Task.objects.all()
        return Task.objects.filter(Q(assigned_to=user) | Q(created_by=user))

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrAssigned]

class TaskMyView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)
