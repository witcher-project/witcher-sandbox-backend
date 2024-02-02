from django.db import models

from ..interfaces import alchemy_interfaces


class Decotion(alchemy_interfaces.BaseAlchemyItemInterface):
    img = models.ImageField(
        upload_to="uploads/items/alchemy/decotions/", default="assets/alchemy/default_decotion.png", null=True
    )
    charges = models.PositiveSmallIntegerField(default=1)
    duration_sec = models.PositiveIntegerField(default=1800)
    tox_points = models.PositiveSmallIntegerField(default=70)


class Potion(alchemy_interfaces.BaseAlchemyItemInterface):
    img = models.ImageField(
        upload_to="uploads/items/alchemy/potions/", default="assets/alchemy/default_potion.png", null=True
    )
    charges = models.PositiveSmallIntegerField(default=3)
    duration_sec = models.PositiveIntegerField(default=30)
    tox_points = models.PositiveSmallIntegerField(default=20)


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
