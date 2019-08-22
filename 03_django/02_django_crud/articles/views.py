from IPython import embed
from django.core.exceptions import ValidationError#예외처리하는...
from django.shortcuts import render, redirect
from .models import Article#현재 디렉토리의 models에 있는 Article

# Create your views here.
def index(request):
    # articles = Article.objects.all()
    articles = Article.objects.order_by('-pk')
    #order_by하면 자동으로 전체 가져오는 거. 이건 DB를 변경
    # articles = Article.objects.all()[::-1]
    # #이건 python이 변경.
    context = {'articles': articles,}

    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    try: #유효성 검사
        title = request.POST.get('title')
        content = request.POST.get('content')
        # #1
        # article = Article()
        # article.title = title
        # article.content = content
        # article.save()

        #2
        article = Article(title=title, content=content)
        #저장되기 전에!
        article.full_clean()
    except ValidationError:#try에서 오류 나면 except동작
        raise ValidationError('Error')
    else:#오류 안 나면
        article.save()
        # #3
        # Article.objects.create(title=title, content=content)
        #얘는 유효성 검사를 할 수가 없음....
        # return render(request, 'articles/index.html')
        return redirect(f'/articles/{article.pk}')


def detail(request, pk):

    article = Article.objects.get(pk=pk)#값이 하나뿐인 pk 찾을 때만 get 쓰기
    context = {'article': article,}
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)#값이 하나뿐인 pk 찾을 때만 get 쓰기
    article.delete()
    return redirect('/articles/')


def edit(request, pk):#뭘 수정할 지 알아야 하니까 pk 받음
    article = Article.objects.get(pk=pk)
    context = {'article': article,}
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')#기존의 인스턴스 변수 값을 새로 할당
    article.content = request.POST.get('content')
    article.save()
    return redirect(f'/articles/{article.pk}/')