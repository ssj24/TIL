from django.urls import path
from . import views#이것도 임포트 하고#현재 파일과 동일선상에 있는 views를 불러온다.


urlpatterns = [
    #app url은 아래로 작성해나간다.
    path('index/', views.index),#이것도 써주고 #url 경로 마지막에 /를 붙이는 습관ended slash
    path('introduce/<str:name>,<int:age>/', views.introduce),
    path('dinner/', views.dinner),
    path('images/', views.image),
    #views의 변수이름 그대로. str은 디폴트라 생략 가능. 다른 타입이면 꼭.
    path('hello/<str:name>/', views.hello),
    path('times/<int:a>*<int:b>/', views.times),
    path('area/<int:r>의 넓이는/', views.area),
    path('template_language/', views.template_language),
    path('gwangbok/', views.isitgwangbok),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('art/', views.art),
    path('result/', views.result),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),
    path('static_example/', views.static_example),
]
