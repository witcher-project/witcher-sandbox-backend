from typing import Any, Optional

from django.db.models import QuerySet
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import BaseSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

from witcher_sandbox.api.permissions import IsOwnerOfObject
from witcher_sandbox.api.serializers.item_image import image_serializers_map


class BaseViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    def get_permissions(self) -> list[Any]:
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAuthenticated, IsOwnerOfObject]
        return [permission() for permission in permission_classes]

    def get_queryset(self) -> QuerySet:
        return self.queryset.order_by("-id")

    def perform_create(self, serializer: BaseSerializer) -> Any:
        return serializer.save(user=self.request.user)


class BaseViewSetImg(BaseViewSet):
    model: Optional[Any] = None

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        if not self.model:
            raise NotImplementedError("model not specified in derived class")

    def get_serializer_class(self) -> list[Any]:
        if self.action == "upload_img":
            return image_serializers_map[self.model]  # type: ignore

        return super().get_serializer_class()

    @action(methods=["POST"], detail=True, url_path="upload-img")
    def upload_img(self, request: Request, pk: Any = None) -> Response:
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
