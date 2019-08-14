"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages import views#이것도 임포트 하고

urlpatterns = [
    path('gwangbok/', views.isitgwangbok),
    path('template_language/', views.template_language),
    path('area/<int:r>의 넓이는/', views.area),
    path('times/<int:a>*<int:b>/', views.times),
    path('hello/<str:name>/', views.hello),
    #views의 변수이름 그대로. str은 디폴트라 생략 가능. 다른 타입이면 꼭.
    path('images/', views.image),
    path('dinner/', views.dinner),
    path('introduce/<str:name>,<int:age>/', views.introduce),
    path('index/', views.index),#이것도 써주고 #url 경로 마지막에 /를 붙이는 습관ended slash
    path('admin/', admin.site.urls),
]
