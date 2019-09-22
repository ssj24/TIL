from django.urls import reverse
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)#기본값이 blank=False
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        # return f'/articles/{self.pk}/'
        # return reverse('articles:detail', args=[self.pk]) 
        return reverse('articles:detail', kwargs={'article_pk':self.pk}) #views.py detail함수의 request와 함께 들어오는 pk
        # return 값은 articles/10/
        # 주의사항
        # reverse 함수에 args랑 kwargs를 동시에 인자로 보낼 수 없다.
    

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE) 
    #ForeignKey가 필드명, 참조하고 있는 객체를 그냥 소문자로. 어차피 얘는 테이블의 마지막에 붙으니까 위치는 무관
    # 실제 컬럼명은 article_id로 나온다
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk']
        # articles = Article.objects.order_by('-pk')로 views.py에서 바꾼 것을
        # models.py에서 바꿀 수 있는 방법. 이 쪽이 더 권장

    def __str__(self):
        # return self.content
        return f'<Article({self.article_id}): Comment({self.pk})-{self.content}'



