from core.views import BaseViewSetImg

from ..models.alchemy_models import Bomb, Decotion, Oil, Potion
from ..models.general_models import CraftingComponent
from ..serializers import alchemy_serializers
from ..serializers.general_serializers import CraftingComponentSerializer


class DecotionViewSet(BaseViewSetImg):
    model = Decotion
    serializer_class = alchemy_serializers.DecotionSerializer
    queryset = Decotion.objects.all()


class PotionViewSet(BaseViewSetImg):
    model = Potion
    serializer_class = alchemy_serializers.PotionSerializer
    queryset = Potion.objects.all()


class OilViewSet(BaseViewSetImg):
    model = Oil
    serializer_class = alchemy_serializers.OilSerializer
    queryset = Oil.objects.all()


class BombViewSet(BaseViewSetImg):
    model = Bomb
    serializer_class = alchemy_serializers.BombSerializer
    queryset = Bomb.objects.all()


class IngredientsViewSet(BaseViewSetImg):
    model = CraftingComponent
    serializer_class = CraftingComponentSerializer
    queryset = CraftingComponent.objects.all()
    # queryset = CraftingComponent.objects.filter(
    #     Q(craft_type=CraftingComponent.CraftType.ALCHEMY) | Q(craft_type=CraftingComponent.CraftType.BOTH)
    # )
