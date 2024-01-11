from core.views import BaseViewSet
from django.http import Http404
from items import serializers
from items.models import CraftingComponent, Recipe, RecipeComponent, Source
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class CraftingComponentViewSet(BaseViewSet):
    serializer_class = serializers.CraftingComponentSerializer
    queryset = CraftingComponent.objects.all()


class RecipeViewSet(BaseViewSet):
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()


class SourceViewSet(BaseViewSet):
    serializer_class = serializers.SourceSerializer
    queryset = Source.objects.all()


class RecipeComponentViewSet(BaseViewSet):
    serializer_class = serializers.RecipeComponentSerializer
    queryset = RecipeComponent.objects.all()

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
