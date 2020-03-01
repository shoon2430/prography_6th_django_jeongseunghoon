from django.contrib import admin
from . import models


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):

    pass


class CommentInline(admin.TabularInline):
    model = models.Comment


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):

    inlines = (CommentInline,)

    list_display = (
        "writer",
        "title",
        "created",
        "updated",
        "count_comments"
    )

    def count_comments(self, obj):
        return obj.commnets.count()
