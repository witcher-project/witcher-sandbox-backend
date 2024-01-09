from alchemy import serializers
from alchemy.models import Bomb, Decotion, Oil, Potion
from core.models import Tier, Type
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
        type = Type.objects.get(id=self.request.data.get("tier"))
        tier = Tier.objects.get(id=self.request.data.get("type"))
        serializer.save(user=self.request.user, type=type, tier=tier)


class DecotionViewSet(BaseViewSet):
    serializer_class = serializers.DecotionSerializer
    queryset = Decotion.objects.all()


class PotionViewSet(BaseViewSet):
    serializer_class = serializers.PotionSerializer
    queryset = Potion.objects.all()


class OilViewSet(BaseViewSet):
    serializer_class = serializers.OilSerializer
    queryset = Oil.objects.all()


class BombViewSet(BaseViewSet):
    serializer_class = serializers.BombSerializer
    queryset = Bomb.objects.all()
