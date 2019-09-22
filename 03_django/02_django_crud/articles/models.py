from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail
from django.urls import reverse
from django.db import models


def articles_image_path(instance, filename):
    return f'articles/{instance.pk}/images/{filename}'

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)#기본값이 blank=False
    content = models.TextField()
    image = ProcessedImageField(
        #ProcessedImageField 에 인자로 들어가 있는 값들은 migrations이후에 추가되거나 수정되더라도 makemigrations를 하지 않아도 된다.
        processors=[Thumbnail(200, 300)], # width, height
        #processor는 처리할 작업 목록 다양한 기능 있으니 찾아보기
        format='JPEG', #저장 포맷
        options={'quality': 90}, #추가 옵션들. 원본 퀄리티의 90%
        upload_to='articles/images',  #저장 위치. 추가 경로. (MEDIA_ROOT)까지 django가 알고 있으니 그 이후의 경로 설정
        )# 나중에 추가한 거라서 중간에 작성해도 실제로는 맨 뒤에 만들어짐
    # image = models.ImageField(blank=True) # 원본이 올라갈 필드
    # image_thumbnail = ImageSpecField( #썸네일이 올라갈 필드 따로 만들어 줌 # 얘는 호출할 때만 동작
    #     source='image', #필수 인자. 뭘 자를 건데? 원본 이미지 필드
    #     processors=[Thumbnail(500, 300)],
    #     format='JPEG',
    #     options={'quality': 90},
    #     # 얘는 업로드 투 없음
    # )
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



