from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('token/', views.CreateTokenAPIView.as_view(), name='token'),
    path('create/', views.CreateUserAPIView.as_view(), name='create'),
]
