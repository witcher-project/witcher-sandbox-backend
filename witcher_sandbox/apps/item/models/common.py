from django.db import models


class Tier(models.Model):
    name = models.CharField(max_length=100, unique=True)
    color_hex = models.CharField(max_length=6, default="FFFFFF")

    def __str__(self) -> str:
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name
