from django.contrib.auth.models import AbstractUser
from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from witcher_sandbox.api.serializers.user import UserSerializer


class CreateUserAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self) -> AbstractUser:
        return self.request.user
