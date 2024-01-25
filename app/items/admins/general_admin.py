from django.contrib import admin

from ..models.general_models import (
    BaseItem,
    CraftingComponent,
    Recipe,
    RecipeComponent,
    Source,
)

admin.site.register(BaseItem)
admin.site.register(CraftingComponent)
admin.site.register(Recipe)
admin.site.register(RecipeComponent)
admin.site.register(Source)
