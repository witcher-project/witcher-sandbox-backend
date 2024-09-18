import django_filters

from witcher_sandbox.api.filters.utils import PriceRangeFilter
from witcher_sandbox.apps.item.models.general import CraftingComponent, Recipe, Source


class CraftingComponentFilter(PriceRangeFilter):
    class Meta:
        model = CraftingComponent
        fields = ["craft_type", "game_id", "name", "tier__name", "type__name", "price"]


class RecipeFilter(django_filters.FilterSet):
    class Meta:
        model = Recipe
        fields = ["item__game_id"]


class SourceFilter(django_filters.FilterSet):
    class Meta:
        model = Source
        fields = ["item__game_id", "source"]
