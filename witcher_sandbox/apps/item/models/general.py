from django.conf import settings
from django.db import models

from witcher_sandbox.apps.item.models.base import BaseItem


class CraftingComponent(BaseItem):
    """
    Represents both: Alchemy ingredients and Crafting components
    """

    class CraftType(models.TextChoices):
        ALCHEMY = "alchemy", "Alchemy"
        CRAFTING = "crafting", "Crafting"
        BOTH = "both", "Both"

    img = models.ImageField(
        upload_to="uploads/item/general/craft_components/",
        default="assets/item/default_craft_component.png",
        null=True,
    )
    craft_type = models.CharField(max_length=50, choices=CraftType.choices)


class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_craft_recipes")
    item = models.ForeignKey(BaseItem, on_delete=models.CASCADE, related_name="craft_recipes")

    def __str__(self) -> str:
        return f"{self.item.name} recipe"


class RecipeComponent(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="components")
    item = models.ForeignKey(BaseItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.quantity} x {self.item} in recipe for {self.recipe.item}"


class Source(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_sources")
    item = models.ForeignKey(BaseItem, on_delete=models.CASCADE, related_name="sources")
    source = models.CharField(max_length=400)
    link = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return f"Source for {self.item.name}"
