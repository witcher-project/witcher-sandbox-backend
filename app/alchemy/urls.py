from alchemy import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = "alchemy"

router = DefaultRouter()
router.register("decotions", views.DecotionViewSet, basename="decotions")
router.register("potions", views.PotionViewSet, basename="potions")
router.register("oils", views.OilViewSet, basename="oils")
router.register("bombs", views.BombViewSet, basename="bombs")
router.register("ingredients", views.IngredientsViewSet, basename="ingredients")

urlpatterns = [path("", include(router.urls))]
