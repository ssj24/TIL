from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): # 커스텀한 유저를 써야 한다고 공식문서가 말한다.
    pass

class Todo(models.Model):
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False) # 처음 등록시 미완료 상태니까 False를 디폴트로
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    