from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["email", "password", "name"]
        extra_kwargs = {"password": {"write_only": True, "min_length": 8}}

    def create(self, validated_data: dict) -> AbstractUser:
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance: AbstractUser, validated_data: dict) -> AbstractUser:
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password),
            user.save()
        return user
