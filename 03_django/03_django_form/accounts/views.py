from IPython import embed
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import authenticate
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
# from django.contrib.auth import login as auth_login, logout as auth_logout 이렇게 이어서 쓸 수도 있음
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST': #유저 만들기
        form = UserCreationForm(request.POST)
        # embed()
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            # form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm # post가 아니면 폼을 띄움
    context = {'form': form}
    return render(request, 'accounts/auth_form.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # embed()
            auth_login(request, form.get_user())
            # embed()
            return redirect(request.GET.get('next') or 'articles:index')
            # next값이 있으면 next값으로, 없으면 index로

    else:
        form = AuthenticationForm()
    context = {'form': form, }
    return render(request, 'accounts/auth_form.html', context)


def logout(request):
    auth_logout(request)
    return redirect('articles:index')

@require_POST
def delete(request):
    request.user.delete()
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {'form': form,}
    return render(request, 'accounts/auth_form.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user) #get방식인데도 request.user가 필수! user정보가 필수라서
    context = {'form': form,}
    return render(request, 'accounts/auth_form.html', context)