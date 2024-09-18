from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from polymorphic.models import PolymorphicModel

from witcher_sandbox.apps.item.models.common import Tier, Type


class BaseItem(PolymorphicModel):
    """
    Consider this model as abstract one and do not communicate with it directly except when writing tests
    it serves only as interface, there are no endpoints to CRUD this model.
    The reason why is not abstract described in documentation.
    """

    game_id = models.CharField(unique=True, max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=3000, blank=True, null=True)
    tier = models.ForeignKey(Tier, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    weight = models.FloatField(validators=[MinValueValidator(0.0)], default=0)
    price = models.PositiveIntegerField()
    fandom_link = models.CharField(max_length=2000, blank=True, null=True)
    is_craftable = models.BooleanField(default=False, blank=True)
    is_dismantlable = models.BooleanField(default=False, blank=True)
    is_usable = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class BaseAlchemyItem(BaseItem):
    charges = models.PositiveSmallIntegerField(default=1)
