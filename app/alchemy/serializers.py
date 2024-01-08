from alchemy.models import Bomb, Decotion, Oil, Potion
from core.models import BaseAlchemyElement
from rest_framework import serializers


class BaseAlchemyElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseAlchemyElement
        fields = ["id", "img", "name", "tier", "type", "price", "source", "link", "effect", "charges", "duration_sec"]
        read_only_fields = ['id']


class DecotionSerializer(serializers.ModelSerializer):
    class Meta(BaseAlchemyElementSerializer):
        model = Decotion
        fields = BaseAlchemyElementSerializer.Meta.fields + ["tox_points"]


class PotionSerializer(serializers.ModelSerializer):
    class Meta(BaseAlchemyElementSerializer):
        model = Potion
        fields = BaseAlchemyElementSerializer.Meta.fields + ["tox_points"]


class OilSerializer(serializers.ModelSerializer):
    class Meta(BaseAlchemyElementSerializer):
        model = Oil
        fields = BaseAlchemyElementSerializer.Meta.fields + ["attack_bonus_perc"]


class BombSerializer(serializers.ModelSerializer):
    class Meta(BaseAlchemyElementSerializer):
        model = Bomb
        fields = BaseAlchemyElementSerializer.Meta.fields
