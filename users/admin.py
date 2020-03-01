from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    ADMIN_FIELDS = UserAdmin.fieldsets
    COSTOM_FIELDS = (
        (
            "CostomFields",
            {
                "fields": (
                    "authority",
                ),
            },
        ),
    )

    fieldsets = ADMIN_FIELDS + COSTOM_FIELDS

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "authority",
    )
