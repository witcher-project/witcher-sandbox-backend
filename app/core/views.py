from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from .permissions import IsOwnerOfObject


class BaseViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAuthenticated, IsOwnerOfObject]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return self.queryset.order_by("-id")

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
