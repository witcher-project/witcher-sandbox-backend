from django.contrib import admin

from witcher_sandbox.apps.item.models import BaseItem, CraftingComponent, Recipe, RecipeComponent, Source, Tier, Type

admin.site.register(BaseItem)
admin.site.register(CraftingComponent)
admin.site.register(Recipe)
admin.site.register(RecipeComponent)
admin.site.register(Source)
admin.site.register(Tier)
admin.site.register(Type)
