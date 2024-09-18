from django.db.models import Q

from witcher_sandbox.api.filters.item_alchemy import BombFilter, IngredientsFilter, OilFilter, PotionFilter
from witcher_sandbox.api.serializers.item_alchemy import BombSerializer, OilSerializer, PotionSerializer
from witcher_sandbox.api.serializers.item_general import CraftingComponentSerializer
from witcher_sandbox.api.views.base import BaseViewSetImg
from witcher_sandbox.apps.item.models.alchemy import Bomb, Oil, Potion
from witcher_sandbox.apps.item.models.general import CraftingComponent


class BasePotionViewSet(BaseViewSetImg):
    model = Potion
    serializer_class = PotionSerializer
    filterset_class = PotionFilter


class DecoctionViewSet(BasePotionViewSet):
    queryset = Potion.objects.filter(potion_type=Potion.PotionType.DECOCTION)


class PotionViewSet(BasePotionViewSet):
    queryset = Potion.objects.filter(potion_type=Potion.PotionType.POTION)


class OilViewSet(BaseViewSetImg):
    model = Oil
    queryset = Oil.objects.all()
    serializer_class = OilSerializer
    filterset_class = OilFilter


class BombViewSet(BaseViewSetImg):
    model = Bomb
    queryset = Bomb.objects.all()
    serializer_class = BombSerializer
    filterset_class = BombFilter


class IngredientsViewSet(BaseViewSetImg):
    model = CraftingComponent
    serializer_class = CraftingComponentSerializer
    queryset = CraftingComponent.objects.filter(
        Q(craft_type=CraftingComponent.CraftType.ALCHEMY) | Q(craft_type=CraftingComponent.CraftType.BOTH)
    )
    filterset_class = IngredientsFilter
