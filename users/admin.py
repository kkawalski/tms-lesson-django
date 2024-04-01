from django.contrib import admin

from users.models import User


# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
    )
    list_display_links = (
        "id",
        "username",
    )
    list_editable = (
        "email",
    )
    list_filter = (
        "is_superuser",
    )
    search_fields = (
        "username",
        "email",
        "last_name",
        "first_name",
    )
    empty_value_display = "..."

    fields = (
        "username",
        "email",
        ("first_name", "last_name")
    )
    # change_list_template = ...
    
