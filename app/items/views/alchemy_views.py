from core.views import BaseViewSet

from ..models.alchemy_models import Bomb, Decotion, Oil, Potion
from ..models.general_models import CraftingComponent
from ..serializers import alchemy_serializers
from ..serializers.general_serializers import CraftingComponentSerializer


class DecotionViewSet(BaseViewSet):
    serializer_class = alchemy_serializers.DecotionSerializer
    queryset = Decotion.objects.all()


class PotionViewSet(BaseViewSet):
    serializer_class = alchemy_serializers.PotionSerializer
    queryset = Potion.objects.all()


class OilViewSet(BaseViewSet):
    serializer_class = alchemy_serializers.OilSerializer
    queryset = Oil.objects.all()


class BombViewSet(BaseViewSet):
    serializer_class = alchemy_serializers.BombSerializer
    queryset = Bomb.objects.all()


class IngredientsViewSet(BaseViewSet):
    # serializer_class = serializers.BaseAlchemyElementSerializer
    # queryset = CraftComponent.objects.all()
    serializer_class = CraftingComponentSerializer
    queryset = CraftingComponent.objects.all()

    # queryset = CraftComponent.objects.filter(craft_type=CraftComponent.CraftType.ALCHEMY)

    # def get_queryset(self):
    #     return CraftComponent.objects.filter(craft_type=CraftComponent.CraftType.ALCHEMY)
