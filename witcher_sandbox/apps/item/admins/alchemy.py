from django.contrib import admin

from ..models.alchemy import Bomb, Oil, Potion

admin.site.register(Potion)
admin.site.register(Oil)
admin.site.register(Bomb)
