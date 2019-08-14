import random
from datetime import datetime
from django.shortcuts import render

# Create your views here.
def index(request):#첫번째 인자는 반드시 request
    return render(request, 'index.html')#render()의 첫번째 인자도 반드시 request


def introduce(request, name, age):
    context = {'name': name, 'age': age, }   
    return render(request, 'introduce.html', context)


def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'pick': pick}#가독성을 위해
    return render(request, 'dinner.html', context)#context가 바로 html에 넘겨줄 값
    #'pick'는 html에서 쓸 값


def image(request):
    return render(request, 'images.html')


def hello(request, name):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'name': name, 'pick_': pick, }
    return render(request, 'hello.html', context)


def times(request, a, b):
    times = a * b
    context = {'a': a, 'b': b, 'times': times,}
    return render(request, 'times.html', context)


def area(request, r):
    area = 3.14*(r**2)
    context = {'r': r,'area': area,}
    return render(request, 'area.html', context)


def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피',]
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'bean']
    datetimenow = datetime.now()
    empty_list= []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list': empty_list,
    }
    return render(request, 'template_language.html', context)


def isitgwangbok(request):
    today = datetime.now()
    if today.month == 8 and today.day == 15:
        result = True
    else:
        result = False
    context = {
        'result': result,
    }
    return render(request, 'gwangbok.html', context)