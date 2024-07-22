from django.contrib import admin

from users.models import User


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ("id", "email", "phone")
    list_filter = ("email", "phone")
    search_fields = ("email", "phone")
