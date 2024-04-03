from django.contrib import admin

from recipies.models import Recipe, FavoriteRecipe, RecipeStep

class RecipeStepInline(admin.TabularInline):
    model = RecipeStep


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
    )
    # list_editable = list_display
    list_display_links = list_display
    inlines = (
        RecipeStepInline,
    )

@admin.register(FavoriteRecipe)
class LikesAdmin(admin.ModelAdmin):
    list_display = (
        "recipe",
        "user",
    )
    # list_editable = list_display


@admin.register(RecipeStep)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "recipe",
        "id",
    )
    # list_editable = list_display
    list_display_links = list_display
