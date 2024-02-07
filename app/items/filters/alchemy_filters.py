from ..models import Bomb, CraftingComponent, Oil, Potion
from .utils import PriceRangeFilter

general_filterset_fields = [
    "game_id",
    "name",
    "tier__name",
    "type__name",
    "craftable",
    "dismantlable",
    "usable",
]


class PotionFilter(PriceRangeFilter):
    class Meta(PriceRangeFilter.Meta):
        model = Potion
        fields = ["duration_sec", "tox_points", "charges"] + general_filterset_fields


class OilFilter(PriceRangeFilter):
    class Meta(PriceRangeFilter.Meta):
        model = Oil
        fields = ["charges"] + general_filterset_fields


class BombFilter(PriceRangeFilter):
    class Meta(PriceRangeFilter.Meta):
        model = Bomb
        fields = ["charges"] + general_filterset_fields


class IngredientsFilter(PriceRangeFilter):
    class Meta(PriceRangeFilter.Meta):
        model = CraftingComponent
        fields = ["craft_type", "game_id"] + general_filterset_fields
