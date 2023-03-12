from django.contrib import admin

from .models import Article, Comment


class CommentInline(admin.StackedInline):
    model = Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline, ]
    list_display = ("title", "author", "data",)


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ("article", "comment", "author",)
