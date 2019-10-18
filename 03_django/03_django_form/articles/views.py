from IPython import embed.0212
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import Http404
from django.views.decorators.http import require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    # articles = get_list_or_404(Article) #이건 글이 하나도 없으면 404에러가 떠서 여기에 쓰기에는 부적절. 
    context = {'articles': articles,}
    return render(request, 'articles/index.html', context)


def create(request):
    # embed()
    if request.method == 'POST':
        # form인스턴스를 생성하고 요청에 의한 데이터를 인자로 받는다. (binding)
        # 이 처리 과정은 binding이라고 불리며, 유효성 체크를 할 수 있도록 해준다.
        form = ArticleForm(request.POST) #들어오는 리퀘스트를 통째로 넣어버림
        # embed()
        # form 유효성 검사
        if form.is_valid():
            # #modelform을 쓰면 cleaned_data필요 없음
            # title = form.cleaned_data.get('title') #cleaned 유효성을 통과한 정제된 데이터
            # content = form.cleaned_data.get('content') #cleaned 유효성을 통과한 정제된 데이터
            # article = Article.objects.create(title=title, content = content)
            article = form.save() #그냥 form을 사용할 때는 쓰지 않던 구문
            return redirect(article)
    else:
        form = ArticleForm()
    #밑에 두 줄이 else구문 안이 아니라는 것!!
    # 상황에 따라 context에 넘어가는 2가지 form
    # 1. GET: 기본 form
    # 2. POST: 검증에 실패 후의 form(is_valid == False일 때)
    context = {'form': form,}
    return render(request, 'articles/form.html', context)


def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all()#comment_set의 comment는 모델명
    comment_form = CommentForm()
    context = {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)
# def detail(request, article_pk):
#     try:
#         article = Article.objects.get(pk=article_pk)
#     except Article.DoesNotExist:
#         raise Http404('No Article matches the given query.')
#     context = {'article': article,}
#     return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')
    

    
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        #수정된 객체와 기존 객체 두 개 모두 불러오는 것
        #그냥 폼은 initial인 게 모델폼은 instance
        if form.is_valid():
            # article.title = form.cleaned_data.get('title')
            # article.content = form.cleaned_data.get('content')
            # article.save()
            article = form.save()
            return redirect(article)
    else:
        # embed()
        # ArticleForm을 초기화(이전에 DB에 저장된 데이터를 넣어준 상태)
        # __dict__ : article 객체 데이터를 딕셔너리 자료형으로 변환
        # form = ArticleForm(initial = article.__dict__)
        # form = ArticleForm(initial={'title': article.title, 'content': article.content})
        form = ArticleForm(instance=article)
    # 1. POST방식일 때 여기 넘어오는 form은 검증에 실패한 form으로 오류 메세지도 포함된 상태
    # 2. GET방식일 때는 초기화된 form
    context = {'form': form, 'article': article,}
    return render(request, 'articles/form.html', context)


# def comments_create(request, article_pk):
#     article = Article.objects.get(pk=article_pk)
#     if request.method == 'POST':
#         form = CommentForm(request.POST) #들어오는 리퀘스트를 통째로 넣어버림
#         if form.is_valid():
#             # comment = form.save() #그냥 form을 사용할 때는 쓰지 않던 구문
#             new_form = form.save(commit=False)
#             new_form.article = article
#             new_form.save()
#             return redirect(article)
#     else:
#         form = CommentForm()
    
#     context = {'form': form,}
#     return render(request, 'articles/form.html', context)

# 선생님은...
@require_POST
def comments_create(request, article_pk):
    # if request.method == 'POST'
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False) #객체를 create하지만, db에 레코드는 작성하지 않는다. save하지 않은 것 모델 속성 바꿀 게 있으면 써 넣으라고
        comment.article_id = article_pk
        comment.save()
    return redirect('articles:detail', article_pk)



@require_POST
def comments_delete(request, article_pk, comment_pk):
    article = Article.objects.get(pk=article_pk)
    
    # if request.method == 'POST':
    comment = get_object_or_404(Comment, pk = comment_pk)
    comment.delete()
    return redirect(article)
    tlswkjdkdmdm 

