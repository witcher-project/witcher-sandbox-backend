from rest_framework import serializers

from .models import Tier, Type


class TierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tier
        fields = ["name", "color_hex"]
        read_only_fields = ["id"]


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ["name"]
        read_only_fields = ["id"]
