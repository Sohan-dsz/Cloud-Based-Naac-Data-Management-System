from django.urls import path
from .views import NAACReportView

app_name = 'reports'

urlpatterns = [
    path('naac/<str:criteria_name>/', NAACReportView.as_view(), name='naac-report'),
]
