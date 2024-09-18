from django.db import models

from witcher_sandbox.apps.item.models.base import BaseAlchemyItem


class Potion(BaseAlchemyItem):
    class PotionType(models.TextChoices):
        POTION = "potion", "Potion"
        DECOCTION = "decoction", "Decoction"

    img = models.ImageField(
        upload_to="uploads/item/alchemy/potions/", default="assets/alchemy/default_potion.png", null=True
    )
    potion_type = models.CharField(max_length=50, choices=PotionType.choices)
    duration_sec = models.PositiveIntegerField()
    tox_points = models.PositiveSmallIntegerField()


class Oil(BaseAlchemyItem):
    img = models.ImageField(upload_to="uploads/item/alchemy/oils/", default="assets/alchemy/default_oil.png", null=True)
    # bonus_against = models.ForeignKey('Monster')
    attack_bonus_perc = models.PositiveSmallIntegerField(default=15)


class Bomb(BaseAlchemyItem):
    img = models.ImageField(
        upload_to="uploads/item/alchemy/decoctions/", default="assets/alchemy/default_bomb.png", null=True
    )
    duration_sec = models.PositiveIntegerField(default=5)
