from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer

from witcher_sandbox.api.serializers.item_alchemy import model_serializer_mapping
from witcher_sandbox.apps.item.models import BaseItem, CraftingComponent, Recipe, RecipeComponent, Source, Tier, Type


class ItemsPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = (model_serializer_mapping,)


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


class SourceSerializer(serializers.ModelSerializer):
    item = serializers.SlugRelatedField(slug_field="game_id", queryset=BaseItem.objects.all())

    class Meta:
        model = Source
        fields = ["id", "item", "source", "link"]
        read_only_fields = ["id"]


class BaseItemSerializer(serializers.ModelSerializer):
    sources = SourceSerializer(many=True, required=False)
    tier = serializers.SlugRelatedField(slug_field="name", queryset=Tier.objects.all())
    type = serializers.SlugRelatedField(slug_field="name", queryset=Type.objects.all())

    class Meta:
        model = BaseItem
        fields = [
            "id",
            "game_id",
            "name",
            "description",
            "tier",
            "type",
            "price",
            "weight",
            "fandom_link",
            "is_craftable",
            "is_dismantlable",
            "sources",
        ]
        abstract = True
        read_only_fields = ["id"]


class RecipeComponentSerializer(serializers.ModelSerializer):
    item = ItemsPolymorphicSerializer

    class Meta:
        model = RecipeComponent
        fields = ["id", "recipe", "item", "quantity"]
        read_only_fields = ["id"]

    def create(self, validated_data: dict) -> RecipeComponent:
        validated_data.pop("user")
        return RecipeComponent.objects.create(**validated_data)


class RecipeSerializer(serializers.ModelSerializer):
    item = ItemsPolymorphicSerializer

    class Meta:
        model = Recipe
        fields = ["id", "item"]
        read_only_fields = ["id"]


class CraftingComponentSerializer(BaseItemSerializer):
    craft_type = serializers.ChoiceField(CraftingComponent.CraftType.choices)

    class Meta(BaseItemSerializer.Meta):
        model = CraftingComponent
        fields = BaseItemSerializer.Meta.fields + ["img", "craft_type"]
        read_only_fields = ["id"]

    def create(self, validated_data: dict) -> CraftingComponent:
        user = self.context["request"].user
        sources = validated_data.pop("sources", [])
        instance = CraftingComponent.objects.create(**validated_data)
        for source in sources:
            instance.sources.add(Source.objects.get_or_create(user=user, **source)[0])
        return instance

    def update(self, instance: CraftingComponent, validated_data: dict) -> CraftingComponent:
        validated_data.pop("sources", [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
