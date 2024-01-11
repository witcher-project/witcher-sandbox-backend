from django.urls import include, path
from items import views
from rest_framework.routers import DefaultRouter

app_name = "items"

router = DefaultRouter()

# connect words for generic purposes  craft-components -> craftcomponents
router.register("crafting-components", views.CraftingComponentViewSet, basename="crafting-components")
router.register("recipes", views.RecipeViewSet, basename="recipes")
router.register("recipes-components", views.RecipeComponentViewSet, basename="recipes-components")
router.register("sources", views.SourceViewSet, basename="sources")  # do I need it ?

urlpatterns = [path("", include(router.urls))]
