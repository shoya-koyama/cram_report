from django.contrib import admin

# Register your models here.

# # admin.py
# from django.contrib import admin
# from import_export import resources
# from import_export.admin import ImportExportMixin
# from import_export.admin import ExportActionModelAdmin  
# from import_export import fields  
# from import_export.widgets import ManyToManyWidget  
# from django.http import HttpResponse
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter
# from reportlab.lib.units import inch
# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.cidfonts import UnicodeCIDFont
# import csv
# import codecs
# from reversion.admin import VersionAdmin



# from .models import Article, Comment

# # 日本語フォントを登録
# pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))

# class ArticleResource(resources.ModelResource):
#     categories = fields.Field(attribute='categories', widget=ManyToManyWidget(Article, field="name"))
#     # Modelに対するdjango-import-exportの設定
#     class Meta:
#         model = Article

# class CommentResource(resources.ModelResource):
#     categories = fields.Field(attribute='categories', widget=ManyToManyWidget(Comment, field="name"))
#     # Modelに対するdjango-import-exportの設定
#     class Meta:
#         model = Comment


# @admin.register(Article)
# class ArticleAdmin(ImportExportMixin, ExportActionModelAdmin, VersionAdmin):
#     # ImportExportModelAdminを利用するようにする
#     ordering = ['id']
#     list_display = ('id', 'title', 'body','posted_at', 'published_at', 'like')

#     # django-import-exportsの設定
#     resource_class = ArticleResource
#     @admin.action(description='Export selected posts as PDF')
#     def pdfer(self, request, queryset):
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="model.pdf"'

#         p = canvas.Canvas(response, pagesize=letter)
#         p.setFont('HeiseiKakuGo-W5', 12)

#         x = 1 * inch
#         y = 10 * inch

#         for post in queryset:
#             p.drawString(x, y, f'Title: {post.title}')
#             p.drawString(x, y - 20, f'Content: {post.body}')
#             p.drawString(x, y - 40, f'Content: {post.posted_at}')
#             p.drawString(x, y - 60, f'Content: {post.published_at}')
#             p.drawString(x, y - 80, f'Content: {post.like}')

#             p.showPage()
#             p.setFont('HeiseiKakuGo-W5', 12)

#         p.save()

#         return response
    
#     def export_action(self, request, queryset):
#         response = super().export_action(request, queryset)
#         response['Content-Type'] = 'text/csv; charset=utf-8'
#         response['Content-Disposition'] = 'attachment; filename="export.csv"'

#         # ヘッダー行を作成する
#         header = [field.verbose_name for field in queryset.model._meta.fields]

#         # カテゴリーごとにデータ行を作成する
#         csv_data = []
#         for obj in queryset:
#             data_row = []
#             for field in obj._meta.fields:
#                 value = field.value_from_object(obj)
#                 if isinstance(value, str):
#                     # 文字列の場合はクォーテーションで囲む
#                     data_row.append('"{0}"'.format(value))
#                 else:
#                     data_row.append(str(value))
#             csv_data.append(data_row)

#         # CSVファイルを作成してresponseに設定する
#         csv_file = codecs.iterencode('\n'.join(','.join(row) for row in [header] + csv_data), 'utf-8-sig')
#         response.content = b','.join(csv_file)

#         return response
#     actions = [pdfer,export_action]

# @admin.register(Comment)
# class CommentAdmin(ImportExportMixin, ExportActionModelAdmin, VersionAdmin):
#     # ImportExportModelAdminを利用するようにする
#     ordering = ['id']
#     list_display = ('id', 'text','posted_at','article')

#     # django-import-exportsの設定
#     resource_class = CommentResource
#     @admin.action(description='Export selected posts as PDF')
#     def pdfer(self, request, queryset):
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="model.pdf"'

#         p = canvas.Canvas(response, pagesize=letter)
  
#         p.setFont('HeiseiKakuGo-W5', 12)

#         x = 1 * inch
#         y = 10 * inch

#         for post in queryset:
#             p.drawString(x, y, f'Title: {post.text}')
#             p.drawString(x, y - 20, f'Content: {post.posted_at}')
#             p.drawString(x, y - 40, f'Content: {post.article}')

#             p.showPage()
#             p.setFont('HeiseiKakuGo-W5', 12)
#         p.save()
#         return response
    
#     def export_action(self, request, queryset):
#         response = super().export_action(request, queryset)
#         response['Content-Type'] = 'text/csv; charset=utf-8'
#         response['Content-Disposition'] = 'attachment; filename="export.csv"'

#         # ヘッダー行を作成する
#         header = [field.verbose_name for field in queryset.model._meta.fields]

#         # カテゴリーごとにデータ行を作成する
#         csv_data = []
#         for obj in queryset:
#             data_row = []
#             for field in obj._meta.fields:
#                 value = field.value_from_object(obj)
#                 if isinstance(value, str):
#                     # 文字列の場合はクォーテーションで囲む
#                     data_row.append('"{0}"'.format(value))
#                 else:
#                     data_row.append(str(value))
#             csv_data.append(data_row)

#         # CSVファイルを作成してresponseに設定する
#         csv_file = codecs.iterencode('\n'.join(','.join(row) for row in [header] + csv_data), 'utf-8-sig')
#         response.content = b','.join(csv_file)

#         return response

#     actions = [pdfer,export_action]