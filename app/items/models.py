from django.conf import settings
from django.db import models
from polymorphic.models import PolymorphicModel


class BaseItem(PolymorphicModel):
    """
    Consider this model as abstract one and do not communicate with it directly except when writing tests
    it serves only as interface, there are no endpoints to CRUD this model.
    The reason why is not abstract described in documentation.
    """

    game_id = models.CharField(unique=True, max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    tier = models.ForeignKey("core.Tier", on_delete=models.PROTECT)
    type = models.ForeignKey("core.Type", on_delete=models.PROTECT)
    weight = models.PositiveSmallIntegerField(default=0, blank=True)
    price = models.PositiveIntegerField()
    link = models.CharField(max_length=2000, blank=True, null=True)
    craftable = models.BooleanField(default=False, blank=True)
    dismantlable = models.BooleanField(default=False, blank=True)
    # more info about item (usually points to WitcherFandom)

    def __str__(self) -> str:
        return self.name


class CraftingComponent(BaseItem):
    """
    Represents both: Alchemy ingridients and Crafting components
    """

    class CraftType(models.TextChoices):
        ALCHEMY = "alchemy", "Alchemy"
        CRAFTING = "crafting", "Crafting"
        BOTH = "both", "Both"

    img = models.ImageField(
        upload_to="items/craft_components/", default="assets/items/default_craft_component.png", null=True
    )
    craft_type = models.CharField(max_length=50, choices=CraftType.choices)


class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_craft_recipes")
    item = models.ForeignKey("items.BaseItem", on_delete=models.CASCADE, related_name="craft_recipes")

    def __str__(self):
        return f"{self.item.name} recipe"


class RecipeComponent(models.Model):
    # doesn't need reference to user because Recipe model already contains user
    recipe = models.ForeignKey("items.Recipe", on_delete=models.CASCADE, related_name="components")
    item = models.ForeignKey("items.BaseItem", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.item} in recipe for {self.recipe.item}"


class Source(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_sources")
    item = models.ForeignKey("items.BaseItem", on_delete=models.CASCADE, related_name="sources")
    source = models.CharField(max_length=400, unique=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.item.name} source"
