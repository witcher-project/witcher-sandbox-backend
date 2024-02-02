from rest_framework.serializers import ModelSerializer

from ..interfaces import alchemy_interfaces
from ..models.alchemy_models import Bomb, Decotion, Oil, Potion


class BaseAlchemyItemSerializer(ModelSerializer):
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


class DecotionSerializer(BaseAlchemyItemSerializer):
    class Meta(BaseAlchemyItemSerializer.Meta):
        model = Decotion
        fields = BaseAlchemyItemSerializer.Meta.fields + ["tox_points", "duration_sec"]


class PotionSerializer(BaseAlchemyItemSerializer):
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
    Decotion: DecotionSerializer,
    Potion: PotionSerializer,
    Oil: OilSerializer,
    Bomb: BombSerializer,
}
