from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import alchemy_views, general_views

app_name = "items"

general_router = DefaultRouter()
general_router.register("crafting-components", general_views.CraftingComponentViewSet, basename="crafting-components")
general_router.register("recipes", general_views.RecipeViewSet, basename="recipes")
general_router.register("recipes-components", general_views.RecipeComponentViewSet, basename="recipes-components")
general_router.register("sources", general_views.SourceViewSet, basename="sources")

alchemy_router = DefaultRouter()
alchemy_router.register("decotions", alchemy_views.DecotionViewSet, basename="decotions")
alchemy_router.register("potions", alchemy_views.PotionViewSet, basename="potions")
alchemy_router.register("oils", alchemy_views.OilViewSet, basename="oils")
alchemy_router.register("bombs", alchemy_views.BombViewSet, basename="bombs")
alchemy_router.register("ingredients", alchemy_views.IngredientsViewSet, basename="ingredients")

urlpatterns = [
    path("general/", include((general_router.urls, "general"), namespace="general")),
    path("alchemy/", include((alchemy_router.urls, "alchemy"), namespace="alchemy")),
]
