from django.db import models

from ..interfaces import alchemy_interfaces


class Potion(alchemy_interfaces.BaseAlchemyItemInterface):
    class PotionType(models.TextChoices):
        POTION = "potion", "Potion"
        DECOTION = "decotion", "Decotion"

    img = models.ImageField(
        upload_to="uploads/items/alchemy/potions/", default="assets/alchemy/default_potion.png", null=True
    )
    potion_type = models.CharField(max_length=50, choices=PotionType.choices)
    charges = models.PositiveSmallIntegerField()
    duration_sec = models.PositiveIntegerField()
    tox_points = models.PositiveSmallIntegerField()


class Oil(alchemy_interfaces.BaseAlchemyItemInterface):
    img = models.ImageField(
        upload_to="uploads/items/alchemy/oils/", default="assets/alchemy/default_oil.png", null=True
    )
    charges = models.PositiveSmallIntegerField(default=30)
    # bonus_against = models.ForeignKey('Monster')
    attack_bonus_perc = models.PositiveSmallIntegerField(default=15)


class Bomb(alchemy_interfaces.BaseAlchemyItemInterface):
    img = models.ImageField(
        upload_to="uploads/items/alchemy/decotions/", default="assets/alchemy/default_bomb.png", null=True
    )
    duration_sec = models.PositiveIntegerField(default=5)
