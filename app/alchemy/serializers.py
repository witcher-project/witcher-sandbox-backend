from alchemy.models import BaseAlchemyElement, Bomb, Decotion, Oil, Potion
from rest_framework import serializers


class BaseAlchemyElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseAlchemyElement
        fields = [
            "id",
            "game_id",
            "img",
            "name",
            "tier",
            "type",
            "price",
            "source",
            "link",
            "effect",
            "charges",
            "duration_sec",
            "craftable",
            "dismantlable",
        ]
        read_only_fields = ["id"]


class DecotionSerializer(serializers.ModelSerializer):
    class Meta(BaseAlchemyElementSerializer.Meta):
        model = Decotion
        fields = BaseAlchemyElementSerializer.Meta.fields + ["tox_points"]


class PotionSerializer(serializers.ModelSerializer):
    class Meta(BaseAlchemyElementSerializer.Meta):
        model = Potion
        fields = BaseAlchemyElementSerializer.Meta.fields + ["tox_points"]


class OilSerializer(serializers.ModelSerializer):
    class Meta(BaseAlchemyElementSerializer.Meta):
        model = Oil
        fields = BaseAlchemyElementSerializer.Meta.fields + ["attack_bonus_perc"]


class BombSerializer(serializers.ModelSerializer):
    class Meta(BaseAlchemyElementSerializer.Meta):
        model = Bomb
        fields = BaseAlchemyElementSerializer.Meta.fields
