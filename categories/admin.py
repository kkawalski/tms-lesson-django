from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from categories.models import Category
from recipies.models import Recipe


class RecipeInline(admin.TabularInline):
    model = Recipe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "parent_link",
    )
    list_display_links = (
        "id",
        "name",
    )
    inlines = (
        RecipeInline,
    )

    def parent_link(self, obj):
        if obj.parent is not None:
            link = reverse('admin:categories_category_change', args=(obj.parent_id,))
            return format_html("<a href='{}'>{}</a>", link, obj.parent.name)
        return None

    parent_link.short_description = "parent"
    
