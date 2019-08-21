from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'cread_at', 'updated_at', )
    list_filter = ('cread_at',)
    list_display_links = ('content', 'pk',)
    list_editable = ('title',)#바로 수정 가능
    list_per_page = 2#default는 100

admin.site.register(Article, ArticleAdmin)