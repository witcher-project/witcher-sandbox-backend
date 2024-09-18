from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from witcher_sandbox.api.views.user import CreateUserAPIView, ManageUserView

# app_name = "user"

urlpatterns = [
    path("me/", ManageUserView.as_view(), name="me"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("create/", CreateUserAPIView.as_view(), name="create"),
]
