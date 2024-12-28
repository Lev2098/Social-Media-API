from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext as _

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with additional fields."""

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "bio", "profile_picture")}),
        (_("Social"), {"fields": ["followers"]}),  # Many-to-Many fields
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser",
                                       "groups", "user_permissions")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2"),
        }),
    )
    list_display = ("email", "first_name", "last_name", "is_staff", "profile_picture")
    search_fields = ("email", "first_name", "last_name", "bio")
    ordering = ("email",)

    # Add filters for the followers and following fields in the admin
    filter_horizontal = ("followers", "groups", "user_permissions")  # Add followers to admin relations
