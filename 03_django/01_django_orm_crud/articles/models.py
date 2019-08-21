from django.db import models

# Create your models here.

class Article(models.Model):#models.Model의 상속을 받는다.
    #id = models.AutoField(primary_key=True)
    #id(프라이머리 키)는 작성하지 않는다. 기본적으로 처음 테이블 생성시
    #자동으로 만들어지기 때문이다.
    #클래스 변수들(db의 필드, 즉 열)
    title = models.CharField(max_length=10)#제목 최대 10자까지
    content = models.TextField()
    cread_at = models.DateTimeField(auto_now_add=True)#작성 시간
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}번글 - {self.title} : {self.content}'