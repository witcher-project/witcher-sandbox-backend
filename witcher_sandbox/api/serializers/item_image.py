from rest_framework import serializers

from witcher_sandbox.apps.item.models import Bomb, CraftingComponent, Oil, Potion


class BaseImageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    img = serializers.ImageField(required=True)

    class Meta:
        fields = ["id", "img"]


class CraftingComponentImageSerializer(BaseImageSerializer, serializers.ModelSerializer):
    class Meta(BaseImageSerializer.Meta):
        model = CraftingComponent
        fields = BaseImageSerializer.Meta.fields


class PotionImageSerializer(BaseImageSerializer, serializers.ModelSerializer):
    class Meta(BaseImageSerializer.Meta):
        model = Potion
        fields = BaseImageSerializer.Meta.fields


class OilImageSerializer(BaseImageSerializer, serializers.ModelSerializer):
    class Meta(BaseImageSerializer.Meta):
        model = Oil
        fields = BaseImageSerializer.Meta.fields


class BombImageSerializer(BaseImageSerializer, serializers.ModelSerializer):
    class Meta(BaseImageSerializer.Meta):
        model = Bomb
        fields = BaseImageSerializer.Meta.fields


image_serializers_map = {
    CraftingComponent: CraftingComponentImageSerializer,
    Potion: PotionImageSerializer,
    Oil: OilImageSerializer,
    Bomb: BombImageSerializer,
}
