from django.urls import path
from . import views#이것도 임포트 하고#현재 파일과 동일선상에 있는 views를 불러온다.


urlpatterns = [
    path('index/', views.index),
]