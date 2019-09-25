from django import forms
from .models import Article, Comment

# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=10, 
#         label='제목',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'my-title', #부트스트랩이면 그 클래스
#                 'placeholder': 'Enter the title',
#             }
#         )
#     ) # models에서 지정한 것과 같이 해 줘야 할 필요는 없지만 같아야겠죠? 그치만 필드는 다르면 안 됨
#     content = forms.CharField(
#         label='내용',
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'my-content',
#                 'placeholder': 'Enter the content',
#                 'rows': 5,
#                 'cols': 50,
#             }
#         )
#     )#forms는 텍스트 필드 없고 캐릭터 필드에서 max_length지정 안 하면 됨.

class ArticleForm(forms.ModelForm): # 모델스에서 textfield여서 얘는 위처럼 설정 안 해줘도 자동으로 textarea로 만들어짐
    title = forms.CharField(
        label='제목',
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title'
            },

        )
    )
    
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        )
    )
    class Meta:#modelform은 class meta가 필수
        model = Article
        # fields = ('title', 'content', )
        fields = '__all__' #all이 아니라 하나씩 쓸 거면 리스트나 튜플로 감싼다
        # exclude = ('title')# fields 안 쓰고 이것만 씀. title외의 모든 것은 다 나오게
        # widgets은 아래와 같이 쓰지 말고 메타 위에 widget으로 쓰는 것을 권장
        # widgets = {
        #     'title': forms.TextInput(attrs={
        #         'class': 'my-title'
        #     })
        # }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)
    