from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDestroyView, TaskMyView

urlpatterns = [
    path('', TaskListCreateView.as_view(), name='task-list-create'),
    path('<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('my/', TaskMyView.as_view(), name='task-my'),
]
