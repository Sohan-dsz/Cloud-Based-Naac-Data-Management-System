from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.conf import settings
from keycloak import KeycloakOpenID
from .models import User, Role
from .serializers import UserSerializer, LoginSerializer, KeycloakTokenSerializer, RoleSerializer


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class KeycloakLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        token_serializer = KeycloakTokenSerializer(data=request.data)
        if not token_serializer.is_valid():
            return Response(token_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        access_token = token_serializer.validated_data['access_token']

        # Initialize Keycloak client
        keycloak_openid = KeycloakOpenID(
            server_url=settings.KEYCLOAK_SERVER_URL,
            client_id=settings.KEYCLOAK_CLIENT_ID,
            realm_name=settings.KEYCLOAK_REALM,
            client_secret_key=settings.KEYCLOAK_CLIENT_SECRET or None
        )

        try:
            # Decode and validate token
            token_info = keycloak_openid.introspect(access_token)
            if not token_info.get('active'):
                return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

            # Get user info
            user_info = keycloak_openid.userinfo(access_token)

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

            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data,
                'message': 'Keycloak login successful'
            })

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class RoleListView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
