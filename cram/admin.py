# admin.py
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Article, Comment

class ArticleResource(resources.ModelResource):
    # Modelに対するdjango-import-exportの設定
    class Meta:
        model = Article

class CommentResource(resources.ModelResource):
    # Modelに対するdjango-import-exportの設定
    class Meta:
        model = Comment


@admin.register(Article)
class ArticleAdmin(ImportExportModelAdmin):
    # ImportExportModelAdminを利用するようにする
    ordering = ['id']
    list_display = ('id', 'title', 'body','posted_at', 'published_at', 'like')

    # django-import-exportsの設定
    resource_class = ArticleResource

@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    # ImportExportModelAdminを利用するようにする
    ordering = ['id']
    list_display = ('id', 'text','posted_at','article')

    # django-import-exportsの設定
    resource_class = CommentResource