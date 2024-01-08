from core.models import BaseAlchemyElement
from django.db import models


class Decotion(BaseAlchemyElement):
    img = models.ImageField(
        upload_to="alchemy/decotions/", default="assets/default_decotion.png"
    )
    charges = models.PositiveSmallIntegerField(default=1)
    duration_sec = models.PositiveIntegerField(default=1800)
    tox_points = models.PositiveSmallIntegerField(default=50)


class Potion(BaseAlchemyElement):
    img = models.ImageField(
        upload_to="alchemy/potions/", default="assets/default_potion.png"
    )
    charges = models.PositiveSmallIntegerField(default=3)
    duration_sec = models.PositiveIntegerField(default=30)
    tox_points = models.PositiveSmallIntegerField(default=20)


class Oil(BaseAlchemyElement):
    img = models.ImageField(upload_to="alchemy/oils/", default="assets/default_oil.png")
    charges = models.PositiveSmallIntegerField(default=30)
    # bonus_against = models.ForeignKey('Monster')
    attack_bonus_perc = models.PositiveSmallIntegerField(default=15)
    duration_sec = None


class Bomb(BaseAlchemyElement):
    img = models.ImageField(
        upload_to="alchemy/bombs/", default="assets/default_bomb.png"
    )
