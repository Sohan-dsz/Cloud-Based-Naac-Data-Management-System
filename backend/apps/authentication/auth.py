import requests
from rest_framework import authentication, exceptions
from django.conf import settings
from .models import User


class KeycloakAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header:
            return None

        try:
            token_type, token = auth_header.split(' ')
            if token_type.lower() != 'bearer':
                return None
        except ValueError:
            return None

        # Validate token with Keycloak
        validation_url = f"{settings.KEYCLOAK_SERVER_URL}/realms/{settings.KEYCLOAK_REALM}/protocol/openid-connect/userinfo"
        headers = {'Authorization': f'Bearer {token}'}

        response = requests.get(validation_url, headers=headers)
        if response.status_code != 200:
            raise exceptions.AuthenticationFailed('Invalid token')

        user_info = response.json()

        # Get or create user
        keycloak_id = user_info.get('sub')
        user, created = User.objects.get_or_create(
            keycloak_id=keycloak_id,
            defaults={
                'username': user_info.get('preferred_username', keycloak_id),
                'email': user_info.get('email', ''),
                'first_name': user_info.get('given_name', ''),
                'last_name': user_info.get('family_name', ''),
            }
        )

        return (user, token)
