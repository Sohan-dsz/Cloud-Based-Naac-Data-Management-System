from django.urls import path
from .views import LoginView, KeycloakLoginView, ProfileView, RoleListView

app_name = 'authentication'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('keycloak-login/', KeycloakLoginView.as_view(), name='keycloak-login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('roles/', RoleListView.as_view(), name='roles'),
]
