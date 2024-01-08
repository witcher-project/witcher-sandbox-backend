from alchemy import serializers
from alchemy.models import Bomb, Decotion, Oil, Potion
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication


class BaseViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return self.queryset.filter(user=user).order_by("-id")
        else:
            return self.queryset.order_by("-id")


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
