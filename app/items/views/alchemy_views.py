from core.views import BaseViewSetImg
from django.db.models import Q

from ..filters import alchemy_filters
from ..models.alchemy_models import Bomb, Decotion, Oil, Potion
from ..models.general_models import CraftingComponent
from ..serializers import alchemy_serializers
from ..serializers.general_serializers import CraftingComponentSerializer


class DecotionViewSet(BaseViewSetImg):
    model = Decotion
    serializer_class = alchemy_serializers.DecotionSerializer
    queryset = Decotion.objects.all()
    filterset_class = alchemy_filters.DecotionFilter


class PotionViewSet(BaseViewSetImg):
    model = Potion
    serializer_class = alchemy_serializers.PotionSerializer
    queryset = Potion.objects.all()
    filterset_class = alchemy_filters.PotionFilter


class OilViewSet(BaseViewSetImg):
    model = Oil
    serializer_class = alchemy_serializers.OilSerializer
    queryset = Oil.objects.all()
    filterset_class = alchemy_filters.OilFilter


class BombViewSet(BaseViewSetImg):
    model = Bomb
    serializer_class = alchemy_serializers.BombSerializer
    queryset = Bomb.objects.all()
    filterset_class = alchemy_filters.BombFilter


class IngredientsViewSet(BaseViewSetImg):
    model = CraftingComponent
    serializer_class = CraftingComponentSerializer
    queryset = CraftingComponent.objects.filter(
        Q(craft_type=CraftingComponent.CraftType.ALCHEMY) | Q(craft_type=CraftingComponent.CraftType.BOTH)
    )
    filterset_class = alchemy_filters.IngredientsFilter
