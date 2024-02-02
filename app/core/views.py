from typing import Any

from items.serializers.image_serializers import image_serializers_map
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
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


class BaseViewSetImg(BaseViewSet):
    model = None

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        if not self.model:
            raise NotImplementedError("model not specified in derived class")

    def get_serializer_class(self):
        if self.action == "upload_img":
            return image_serializers_map[self.model]

        return super().get_serializer_class()

    @action(methods=["POST"], detail=True, url_path="upload-img")
    def upload_img(self, request, pk=None) -> Response:
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
