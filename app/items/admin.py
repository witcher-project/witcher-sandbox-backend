# from django.contrib import admin

# from .models import CraftComponent, Recipe, RecipeComponent, Tier, Type

# admin.site.register(Tier)
# admin.site.register(Type)
# admin.site.register(RecipeComponent)
# admin.site.register(CraftComponent)
# admin.site.register(Recipe)

from django.contrib import admin

from .models import BaseItem, CraftingComponent, Recipe, RecipeComponent, Source

admin.site.register(BaseItem)
admin.site.register(CraftingComponent)
admin.site.register(Recipe)
admin.site.register(RecipeComponent)
admin.site.register(Source)
