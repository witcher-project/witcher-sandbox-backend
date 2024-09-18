from django.urls import include, path
from rest_framework.routers import DefaultRouter

from witcher_sandbox.api.views import item_alchemy, item_general

# app_name = "item"

general_router = DefaultRouter()
general_router.register("crafting-components", item_general.CraftingComponentViewSet, basename="crafting-components")
general_router.register("recipes", item_general.RecipeViewSet, basename="recipes")
general_router.register("recipes-components", item_general.RecipeComponentViewSet, basename="recipes-components")
general_router.register("sources", item_general.SourceViewSet, basename="sources")

alchemy_router = DefaultRouter()
alchemy_router.register("decoctions", item_alchemy.DecoctionViewSet, basename="decoctions")
alchemy_router.register("potions", item_alchemy.PotionViewSet, basename="potions")
alchemy_router.register("oils", item_alchemy.OilViewSet, basename="oils")
alchemy_router.register("bombs", item_alchemy.BombViewSet, basename="bombs")
alchemy_router.register("ingredients", item_alchemy.IngredientsViewSet, basename="ingredients")

urlpatterns = [
    path("general/", include((general_router.urls, "general"), namespace="general")),
    path("alchemy/", include((alchemy_router.urls, "alchemy"), namespace="alchemy")),
]
