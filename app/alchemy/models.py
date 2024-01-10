from core.models import BaseItem
from django.db import models


class BaseAlchemyElement(BaseItem):
    wgt = None
    lvl = None
    effect = models.CharField(max_length=2000)
    charges = models.PositiveSmallIntegerField(default=1)
    duration_sec = models.PositiveIntegerField(default=1800)

    class Meta:
        abstract = True


class Decotion(BaseAlchemyElement):
    img = models.ImageField(upload_to="alchemy/decotions/", default="assets/default_decotion.png", null=True)
    charges = models.PositiveSmallIntegerField(default=1)
    duration_sec = models.PositiveIntegerField(default=1800)
    tox_points = models.PositiveSmallIntegerField(default=70)


class Potion(BaseAlchemyElement):
    img = models.ImageField(upload_to="alchemy/potions/", default="assets/default_potion.png", null=True)
    charges = models.PositiveSmallIntegerField(default=3)
    duration_sec = models.PositiveIntegerField(default=30)
    tox_points = models.PositiveSmallIntegerField(default=20)


class Oil(BaseAlchemyElement):
    img = models.ImageField(upload_to="alchemy/oils/", default="assets/default_oil.png", null=True)
    charges = models.PositiveSmallIntegerField(default=30)
    # bonus_against = models.ForeignKey('Monster')
    attack_bonus_perc = models.PositiveSmallIntegerField(default=15)
    duration_sec = None


class Bomb(BaseAlchemyElement):
    img = models.ImageField(upload_to="alchemy/bombs/", default="assets/default_bomb.png", null=True)
