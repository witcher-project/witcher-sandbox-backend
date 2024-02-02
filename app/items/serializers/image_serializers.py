from items.models import Bomb, CraftingComponent, Decotion, Oil, Potion
from rest_framework import serializers


class BaseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        fields = ["id", "img"]
        read_only_fields = ["id"]
        extra_kwargs = {"img": {"required": True}}


class CraftingComponentImageSerializer(BaseImageSerializer):
    class Meta(BaseImageSerializer.Meta):
        model = CraftingComponent


class DecotionComponentImageSerializer(BaseImageSerializer):
    class Meta(BaseImageSerializer.Meta):
        model = Decotion


class PotionComponentImageSerializer(BaseImageSerializer):
    class Meta(BaseImageSerializer.Meta):
        model = Potion


class OilComponentImageSerializer(BaseImageSerializer):
    class Meta(BaseImageSerializer.Meta):
        model = Oil


class BombComponentImageSerializer(BaseImageSerializer):
    class Meta(BaseImageSerializer.Meta):
        model = Bomb


image_serializers_map = {
    CraftingComponent: CraftingComponentImageSerializer,
    Decotion: DecotionComponentImageSerializer,
    Potion: PotionComponentImageSerializer,
    Oil: OilComponentImageSerializer,
    Bomb: BombComponentImageSerializer,
}
