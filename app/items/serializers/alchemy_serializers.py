from core.models import Tier, Type
from rest_framework import serializers

from ..interfaces import alchemy_interfaces
from ..models.alchemy_models import Bomb, Oil, Potion
from .fields import SourceField


class BaseAlchemyItemSerializer(serializers.ModelSerializer):
    sources = SourceField(many=True, read_only=True)

    class Meta:
        model = alchemy_interfaces.BaseAlchemyItemInterface
        fields = [
            "id",
            "game_id",
            "img",
            "name",
            "tier",
            "type",
            "price",
            "weight",
            "link",
            "craftable",
            "dismantlable",
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
