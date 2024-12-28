from django.contrib import admin

from social_media_action.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "content", "created_at", "updated_at")
    search_fields = ("user__username", "content")
    list_filter = ("updated_at", "created_at")
    fields = ("user", "content", "media", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
