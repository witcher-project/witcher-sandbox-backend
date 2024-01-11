from alchemy import serializers
from alchemy.models import Bomb, Decotion, Oil, Potion
from core.views import BaseViewSet
from items.models import CraftingComponent
from items.serializers import CraftingComponentSerializer


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


class IngredientsViewSet(BaseViewSet):
    # serializer_class = serializers.BaseAlchemyElementSerializer
    # queryset = CraftComponent.objects.all()
    serializer_class = CraftingComponentSerializer
    queryset = CraftingComponent.objects.all()

    # queryset = CraftComponent.objects.filter(craft_type=CraftComponent.CraftType.ALCHEMY)

    # def get_queryset(self):
    #     return CraftComponent.objects.filter(craft_type=CraftComponent.CraftType.ALCHEMY)
