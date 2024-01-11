from alchemy.models import BaseAlchemyItem, Bomb, Decotion, Oil, Potion
from rest_framework import serializers


class BaseAlchemyItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseAlchemyItem
        fields = [
            "id",
            "game_id",
            "name",
            "tier",
            "type",
            "price",
            "weight",
            "link",
            "craftable",
            "dismantlable",
            "sources",
            "effect",
            "charges",
            "duration_sec",
        ]


class DecotionSerializer(BaseAlchemyItemSerializer):
    class Meta(BaseAlchemyItemSerializer.Meta):
        model = Decotion
        fields = BaseAlchemyItemSerializer.Meta.fields + ["tox_points"]


class PotionSerializer(BaseAlchemyItemSerializer):
    class Meta(BaseAlchemyItemSerializer.Meta):
        model = Potion
        fields = BaseAlchemyItemSerializer.Meta.fields + ["tox_points"]


class OilSerializer(BaseAlchemyItemSerializer):
    class Meta(BaseAlchemyItemSerializer.Meta):
        model = Oil
        fields = BaseAlchemyItemSerializer.Meta.fields + ["attack_bonus_perc"]


class BombSerializer(BaseAlchemyItemSerializer):
    class Meta(BaseAlchemyItemSerializer.Meta):
        model = Bomb
        fields = BaseAlchemyItemSerializer.Meta.fields
