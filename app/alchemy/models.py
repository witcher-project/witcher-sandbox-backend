from django.db import models
from items.models import BaseItem


class BaseAlchemyItem(BaseItem):
    effect = models.CharField(max_length=2000)
    charges = models.PositiveSmallIntegerField(default=1)
    duration_sec = models.PositiveIntegerField(default=1800)

    class Meta:
        abstract = True


class Decotion(BaseAlchemyItem):
    img = models.ImageField(upload_to="alchemy/decotions/", default="assets/alchemy/default_decotion.png", null=True)
    charges = models.PositiveSmallIntegerField(default=1)
    duration_sec = models.PositiveIntegerField(default=1800)
    tox_points = models.PositiveSmallIntegerField(default=70)


class Potion(BaseAlchemyItem):
    img = models.ImageField(upload_to="alchemy/potions/", default="assets/alchemy/default_potion.png", null=True)
    charges = models.PositiveSmallIntegerField(default=3)
    duration_sec = models.PositiveIntegerField(default=30)
    tox_points = models.PositiveSmallIntegerField(default=20)


class Oil(BaseAlchemyItem):
    img = models.ImageField(upload_to="alchemy/oils/", default="assets/alchemy/default_oil.png", null=True)
    charges = models.PositiveSmallIntegerField(default=30)
    # bonus_against = models.ForeignKey('Monster')
    attack_bonus_perc = models.PositiveSmallIntegerField(default=15)
    duration_sec = None


class Bomb(BaseAlchemyItem):
    img = models.ImageField(upload_to="alchemy/bombs/", default="assets/alchemy/default_bomb.png", null=True)
    duration_sec = models.PositiveIntegerField(default=5)
