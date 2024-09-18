from django.http import Http404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from witcher_sandbox.api.filters.item_general import CraftingComponentFilter, RecipeFilter, SourceFilter
from witcher_sandbox.api.serializers.item_general import (
    CraftingComponentSerializer,
    RecipeComponentSerializer,
    RecipeSerializer,
    SourceSerializer,
)
from witcher_sandbox.api.views.base import BaseViewSet, BaseViewSetImg
from witcher_sandbox.apps.item.models.general import CraftingComponent, Recipe, RecipeComponent, Source


class CraftingComponentViewSet(BaseViewSetImg):
    model = CraftingComponent
    queryset = CraftingComponent.objects.all()
    serializer_class = CraftingComponentSerializer
    filterset_class = CraftingComponentFilter


class RecipeViewSet(BaseViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filterset_class = RecipeFilter


class SourceViewSet(BaseViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    filterset_class = SourceFilter


class RecipeComponentViewSet(BaseViewSet):
    queryset = RecipeComponent.objects.all()
    serializer_class = RecipeComponentSerializer

    def get_permissions(self) -> list:
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_destroy(self, instance: RecipeComponent) -> None | Http404:
        if instance.recipe.user == self.request.user:
            return super().perform_destroy(instance)
        raise Http404
