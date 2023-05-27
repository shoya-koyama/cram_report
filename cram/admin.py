# admin.py
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin,ImportExportMixin, ExportMixin , ImportMixin  #修正
from import_export.admin import ExportActionModelAdmin   #追加
from import_export import fields   #追加
from import_export.widgets import ManyToManyWidget   #追加
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont


from .models import Article, Comment

# 日本語フォントを登録
pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))

class ArticleResource(resources.ModelResource):
    categories = fields.Field(attribute='categories', widget=ManyToManyWidget(Article, field="name"))
    # Modelに対するdjango-import-exportの設定
    class Meta:
        model = Article

class CommentResource(resources.ModelResource):
    categories = fields.Field(attribute='categories', widget=ManyToManyWidget(Comment, field="name"))
    # Modelに対するdjango-import-exportの設定
    class Meta:
        model = Comment


@admin.register(Article)
class ArticleAdmin(ImportExportMixin, ExportActionModelAdmin, admin.ModelAdmin):
    # ImportExportModelAdminを利用するようにする
    ordering = ['id']
    list_display = ('id', 'title', 'body','posted_at', 'published_at', 'like')

    # django-import-exportsの設定
    resource_class = ArticleResource
    @admin.action(description='Export selected posts as PDF')
    def export_as_pdf(self, request, queryset):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="posts.pdf"'

        p = canvas.Canvas(response, pagesize=letter)

        # 日本語フォントを指定
        p.setFont('HeiseiKakuGo-W5', 12)

        x = 1 * inch
        y = 10 * inch

        for post in queryset:
            p.drawString(x, y, f'Title: {post.title}')
            p.drawString(x, y - 20, f'Content: {post.body}')
            p.drawString(x, y - 40, f'Content: {post.posted_at}')
            p.drawString(x, y - 60, f'Content: {post.published_at}')
            p.drawString(x, y - 80, f'Content: {post.like}')

            p.showPage()

            # 新しいページのためにフォントを再設定
            p.setFont('HeiseiKakuGo-W5', 12)

        p.save()

        return response

    actions = [export_as_pdf]

@admin.register(Comment)
class CommentAdmin(ImportExportMixin, ExportActionModelAdmin, admin.ModelAdmin):
    # ImportExportModelAdminを利用するようにする
    ordering = ['id']
    list_display = ('id', 'text','posted_at','article')

    # django-import-exportsの設定
    resource_class = CommentResource
    @admin.action(description='Export selected posts as PDF')
    def export_as_pdf(self, request, queryset):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="posts.pdf"'

        p = canvas.Canvas(response, pagesize=letter)

        # 日本語フォントを指定
        p.setFont('HeiseiKakuGo-W5', 12)

        x = 1 * inch
        y = 10 * inch

        for post in queryset:
            p.drawString(x, y, f'Title: {post.text}')
            p.drawString(x, y - 20, f'Content: {post.posted_at}')
            p.drawString(x, y - 40, f'Content: {post.article}')

            p.showPage()

            # 新しいページのためにフォントを再設定
            p.setFont('HeiseiKakuGo-W5', 12)

        p.save()

        return response

    actions = [export_as_pdf]