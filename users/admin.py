from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from .import models as user_models


@admin.register(user_models.User)
class UserAdmin(UserAdmin):

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            _("Important dates"),
            {
                "fields": (
                    "fcm_token",
                    "last_login",
                    "date_joined",
                    "email_varified",
                    "phone_varified",
                    "login_method",
                )
            },
        ),
    )

    list_display = ("id", "email", "first_name", "last_name", "is_staff")
    search_fields = ("email", "first_name", "last_name")
