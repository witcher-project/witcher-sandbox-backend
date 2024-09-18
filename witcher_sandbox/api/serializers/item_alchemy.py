from rest_framework import serializers

from witcher_sandbox.api.serializers.fields import ItemSourceField
from witcher_sandbox.apps.item.models import BaseAlchemyItem, Tier, Type

# from witcher_sandbox.api.interfaces import item_alchemy
from witcher_sandbox.apps.item.models.alchemy import Bomb, Oil, Potion


class BaseAlchemyItemSerializer(serializers.ModelSerializer):
    sources = ItemSourceField(many=True, read_only=True)

    class Meta:
        model = BaseAlchemyItem
        fields = [
            "id",
            "game_id",
            "img",
            "name",
            "tier",
            "type",
            "price",
            "weight",
            "fandom_link",
            "is_craftable",
            "is_dismantlable",
            "sources",
            "charges",
        ]

    abstract = True


class PotionSerializer(BaseAlchemyItemSerializer):
    tier = serializers.SlugRelatedField(slug_field="name", queryset=Tier.objects.all())
    type = serializers.SlugRelatedField(slug_field="name", queryset=Type.objects.all())

    class Meta(BaseAlchemyItemSerializer.Meta):
        model = Potion
        fields = BaseAlchemyItemSerializer.Meta.fields + ["tox_points", "duration_sec"]


class OilSerializer(BaseAlchemyItemSerializer):
    class Meta(BaseAlchemyItemSerializer.Meta):
        model = Oil
        fields = BaseAlchemyItemSerializer.Meta.fields + ["attack_bonus_perc"]


class BombSerializer(BaseAlchemyItemSerializer):
    class Meta(BaseAlchemyItemSerializer.Meta):
        model = Bomb
        fields = BaseAlchemyItemSerializer.Meta.fields + ["duration_sec"]


model_serializer_mapping = {
    Potion: PotionSerializer,
    Oil: OilSerializer,
    Bomb: BombSerializer,
}
