from core.views import BaseViewSetImg
from django.db.models import Q

from ..filters import alchemy_filters
from ..models.alchemy_models import Bomb, Oil, Potion
from ..models.general_models import CraftingComponent
from ..serializers import alchemy_serializers
from ..serializers.general_serializers import CraftingComponentSerializer


class BasePotionViewSet(BaseViewSetImg):
    model = Potion
    serializer_class = alchemy_serializers.PotionSerializer
    filterset_class = alchemy_filters.PotionFilter


class DecotionViewSet(BasePotionViewSet):
    queryset = Potion.objects.filter(potion_type=Potion.PotionType.DECOTION)


class PotionViewSet(BasePotionViewSet):
    queryset = Potion.objects.filter(potion_type=Potion.PotionType.POTION)


class OilViewSet(BaseViewSetImg):
    model = Oil
    queryset = Oil.objects.all()
    serializer_class = alchemy_serializers.OilSerializer
    filterset_class = alchemy_filters.OilFilter


class BombViewSet(BaseViewSetImg):
    model = Bomb
    queryset = Bomb.objects.all()
    serializer_class = alchemy_serializers.BombSerializer
    filterset_class = alchemy_filters.BombFilter


class IngredientsViewSet(BaseViewSetImg):
    model = CraftingComponent
    serializer_class = CraftingComponentSerializer
    queryset = CraftingComponent.objects.filter(
        Q(craft_type=CraftingComponent.CraftType.ALCHEMY) | Q(craft_type=CraftingComponent.CraftType.BOTH)
    )
    filterset_class = alchemy_filters.IngredientsFilter
