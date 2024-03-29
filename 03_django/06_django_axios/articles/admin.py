from django.contrib import admin
from .models import Article, Comment, Hashtag

# Register your models here.

#마이그레이션 후 슈퍼유저 만들고 그걸 어드민에 등록

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)


# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'content', 'created_at', 'updated_at', 'article_id', )

# admin.site.register(Comment, CommentAdmin)


#위에 거와 밑에 거가 똑같음. 데코레이터 이용
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'created_at', 'updated_at', 'article_id', )

    
class HashtagAdmin(admin.ModelAdmin):
    list_display = ('content',)

admin.site.register(Hashtag, HashtagAdmin)