from alchemy import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = "alchemy"

router = DefaultRouter()
router.register("decotions", views.DecotionViewSet)
router.register("potions", views.PotionViewSet)
router.register("oils", views.OilViewSet)
router.register("bombs", views.BombViewSet)

urlpatterns = [path("", include(router.urls))]
