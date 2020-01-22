from django.contrib import admin

from . import models


# TabularInline view
class CommentInline(admin.TabularInline):
    model = models.Comment


# StackedInline view
# class CommentInline(admin.StackedInline):
#     model = models.Comment


class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


admin.site.register(models.Articles, ArticleAdmin)
admin.site.register(models.Comment)
