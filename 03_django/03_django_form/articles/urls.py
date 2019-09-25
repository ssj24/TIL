from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/update/', views.update, name='update'),
    path('<int:article_pk>/comments/', views.comments_create, name='comments_create'), # DETAIL(GET) + CREATE(POST)
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comments_delete, name='comments_delete'), #url을 통해서 요청을 받으니까 url에 필요한 인자가 다 나와있어야 한다.
]
