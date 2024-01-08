from django.conf import settings
from django.db import models


class BaseItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="items/", default="assets/default_item.png")
    name = models.CharField(max_length=500)
    tier = models.ForeignKey("core.Tier", on_delete=models.PROTECT)
    type = models.ForeignKey("core.Type", on_delete=models.PROTECT)
    wgt = models.PositiveSmallIntegerField(default=0)
    lvl = models.PositiveSmallIntegerField(default=1)
    price = models.PositiveIntegerField()
    source = models.CharField(max_length=2000)
    link = models.CharField(max_length=2000, blank=True, null=True)
    # more info about item (usually points to WitcherFandom)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name


class BaseAlchemyElement(BaseItem):
    wgt = None
    lvl = None
    effect = models.CharField(max_length=2000)
    charges = models.PositiveSmallIntegerField(default=1)
    duration_sec = models.PositiveIntegerField(default=1800)

    class Meta:
        abstract = True


class Tier(models.Model):
    name = models.CharField(max_length=100)
    color_hex = models.CharField(max_length=6, default="FFFFFF")
    # relict
    # common
    # magic

    def __str__(self) -> str:
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100)
    # horse equipment
    # alchemy ingridient
    # Steel Sword
    # Silver Sword
    # Potion

    def __str__(self) -> str:
        return self.name


# class Label(models.Model):
#     # recommended
#     # hard to obtain
#     # unique
#     pass


# class Category(models.Model):
#     # in game item
#     # custom item (made by users of our service)
#     pass
