from django.contrib import admin

from recipies.models import Recipe, FavoriteRecipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
    )
    # list_editable = list_display
    list_display_links = list_display

@admin.register(FavoriteRecipe)
class LikesAdmin(admin.ModelAdmin):
    list_display = (
        "recipe",
        "user",
    )
    # list_editable = list_display
