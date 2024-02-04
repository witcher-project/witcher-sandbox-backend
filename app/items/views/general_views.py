from core.views import BaseViewSet, BaseViewSetImg
from django.http import Http404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from ..filters import general_filters
from ..models.general_models import CraftingComponent, Recipe, RecipeComponent, Source
from ..serializers import general_serializers


class CraftingComponentViewSet(BaseViewSetImg):
    model = CraftingComponent
    queryset = CraftingComponent.objects.all()
    serializer_class = general_serializers.CraftingComponentSerializer
    filterset_class = general_filters.CraftingComponentFilter


class RecipeViewSet(BaseViewSet):
    queryset = Recipe.objects.all()
    serializer_class = general_serializers.RecipeSerializer
    filterset_class = general_filters.RecipeFilter


class SourceViewSet(BaseViewSet):
    queryset = Source.objects.all()
    serializer_class = general_serializers.SourceSerializer
    filterset_class = general_filters.SourceFilter


class RecipeComponentViewSet(BaseViewSet):
    queryset = RecipeComponent.objects.all()
    serializer_class = general_serializers.RecipeComponentSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_destroy(self, instance):
        if instance.recipe.user == self.request.user:
            return super().perform_destroy(instance)
        raise Http404
