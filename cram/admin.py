# admin.py
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Article

class ArticleResource(resources.ModelResource):
    # Modelに対するdjango-import-exportの設定
    class Meta:
        model = Article


@admin.register(Article)
class ArticleAdmin(ImportExportModelAdmin):
    # ImportExportModelAdminを利用するようにする
    ordering = ['id']
    list_display = ('id', 'title', 'body')

    # django-import-exportsの設定
    resource_class = ArticleResource