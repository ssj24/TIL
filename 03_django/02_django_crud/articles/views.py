from IPython import embed
from django.core.exceptions import ValidationError#예외처리하는...
from django.shortcuts import render, redirect
from .models import Article, Comment#현재 디렉토리의 models에 있는 Article

# Create your views here.
def index(request):
    # embed()
    # articles = Article.objects.all()
    articles = Article.objects.order_by('-pk')
    #order_by하면 자동으로 전체 가져오는 거. 이건 DB를 변경
    # articles = Article.objects.all()[::-1]
    # #이건 python이 변경.
    context = {'articles': articles,}

    return render(request, 'articles/index.html', context)


# def new(request):
#     return render(request, 'articles/new.html')


def create(request):
    #CREATE
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image') #이미지 추가! FILES
        article = Article(title=title, content=content, image=image)
        article.save()
        # embed()
        return redirect(article)
        # return redirect('articles:detail', article.pk)
    #NEW
    else:
        return render(request, 'articles/create.html')
    
    # # embed()
    # try: #유효성 검사
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     # #1
    #     # article = Article()
    #     # article.title = title
    #     # article.content = content
    #     # article.save()

    #     #2
    #     article = Article(title=title, content=content)
    #     #저장되기 전에!
    #     article.full_clean()
    # except ValidationError:#try에서 오류 나면 except동작
    #     raise ValidationError('Error')
    # else:#오류 안 나면
    #     article.save()
    #     # #3
    #     # Article.objects.create(title=title, content=content)
    #     #얘는 유효성 검사를 할 수가 없음....
    #     # return render(request, 'articles/index.html')
    #     return redirect('articles:detail', article.pk)



def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)#값이 하나뿐인 pk 찾을 때만 get 쓰기
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comments': comments,
        }
    return render(request, 'articles/detail.html', context)


def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)#값이 하나뿐인 pk 찾을 때만 get 쓰기
    if request.method == 'POST': #post 방식으로 삭제할 때만 되게. url에서 바로 지우지 못하게 하는 것
        article.delete()
        return redirect('articles:index')
    else:
        return redirect(article)
        # return redirect('articles:detail', article.pk)


def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')#기존의 인스턴스 변수 값을 새로 할당
        article.content = request.POST.get('content')
        article.image = request.FILES.get('image')
        article.save()
        return redirect(article) #get_absolute_url을 쓰면 객체만 넣어주면 detail로..!
        # return redirect('articles:detail', article.pk)
    else:
        context = {'article': article,}
        return render(request, 'articles/update.html', context)


# def edit(request, pk):#뭘 수정할 지 알아야 하니까 pk 받음
#     article = Article.objects.get(pk=pk)
#     context = {'article': article,}
#     return render(request, 'articles/edit.html', context)


# def update(request, pk):
#     article = Article.objects.get(pk=pk)
#     article.title = request.POST.get('title')#기존의 인스턴스 변수 값을 새로 할당
#     article.content = request.POST.get('content')
#     article.save()
#     return redirect('articles:detail', article.pk)


def comments_create(request, article_pk): 
    # 게시글의 pk를 가지고 오는 것. 그냥 이걸 표시해주는 거. 본인이 알아서 결정. 댓글 pk와 구분하기 위해서
    # url의 pk도 바꿔줘야 합니다
    # models.py의 get_absolute_url도..
    # 댓글을 달 게시글 필요
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        # form에서 넘어온 댓글 정보
        content = request.POST.get('content')
        # 댓글 생성 및 저장
        comment = Comment(article=article, content=content)# article의 pk 값을..!
        comment.save()
        return redirect(article)
        # 하기 두 개도 동일
        # return redirect('articles:detail' article.pk)
        # return redirect('articles:detail' article_pk)

    else:
        return redirect(article)


# def comments_delete(request, article_pk, comment_pk):
#     article = Article.objects.get(pk=article_pk)
#     comment = Comment.objects.get(pk=comment_pk)
#     if request.method == 'POST':
#         comment.delete()
#     return redirect(article)
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        comment.delete()
    return redirect('articles:detail', article_pk)
    # 얘가 쿼리 하나 안 날리니까 조금 더 빠름