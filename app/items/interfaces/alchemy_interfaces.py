from django.db import models

from ..models.general_models import BaseItem


class BaseAlchemyItemInterface(BaseItem):
    charges = models.PositiveSmallIntegerField(default=1)

    class Meta:
        abstract = True
