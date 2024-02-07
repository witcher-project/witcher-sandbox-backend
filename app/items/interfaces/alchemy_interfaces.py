from django.db import models

from ..models.general_models import BaseItem


class BaseAlchemyItemInterface(BaseItem):
    """
    Helps to avoid circular import error and provide additional fields to alchemy items.
    """

    charges = models.PositiveSmallIntegerField(default=1)

    class Meta:
        abstract = True
