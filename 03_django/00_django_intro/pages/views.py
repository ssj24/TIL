import random
import requests
from datetime import datetime
from pprint import pprint
from django.shortcuts import render

# Create your views here.
def index(request):#첫번째 인자는 반드시 request
    return render(request, 'pages/index.html')#render()의 첫번째 인자도 반드시 request


def introduce(request, name, age):
    context = {'name': name, 'age': age, }   
    return render(request, 'pages/introduce.html', context)


def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'pick': pick}#가독성을 위해
    return render(request, 'pages/dinner.html', context)#context가 바로 html에 넘겨줄 값
    #'pick'는 html에서 쓸 값


def image(request):
    return render(request, 'pages/images.html')


def hello(request, name):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'name': name, 'pick_': pick, }
    return render(request, 'pages/hello.html', context)


def times(request, a, b):
    times = a * b
    context = {'a': a, 'b': b, 'times': times,}
    return render(request, 'pages/times.html', context)


def area(request, r):
    area = 3.14*(r**2)
    context = {'r': r,'area': area,}
    return render(request, 'pages/area.html', context)


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
    return render(request, 'pages/template_language.html', context)


def isitgwangbok(request):
    today = datetime.now()
    if today.month == 8 and today.day == 15:
        result = True
    else:
        result = False
    context = {
        'result': result,
    }
    return render(request, 'pages/gwangbok.html', context)


def throw(request):
    return render(request, 'pages/throw.html')


def catch(request):
    #https://docs.djangoproject.com/en/2.2/ref/request-response/
    # pprint(request)
    # pprint(request.scheme)
    # pprint(request.path)
    # pprint(request.method)
    # pprint(request.GET)
    pprint(request.META)#request의 모든 정보
    # get방식으로 넘어오는 message(인풋의 name)를 딕셔너리라 이렇게 받음
    message = request.GET.get('message')
    # message = request.GET['message']이렇게 쓰면 항목 없으면 에러
    context = {'message': message,}
    return render(request, 'pages/catch.html', context)


def art(request):
    return render(request, 'pages/art.html')


def result(request):
    #http://artii.herokuapp.com/
    word = request.GET.get('word')
    #artii api의 폰트 리스트로 요청을 보내 응답을 text로 받는다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    #얻어온 문자열을 엔터를 기준으로 리스트로 바꾼다.
    fonts = fonts.split('\n')
    #fonts list 안에 들어이쓴ㄴ 요소 중 하나를 선택해서 변수에 저장
    font = random.choice(fonts)
    #위에서 만든 word와 font를 가지고 다시 요청을 만들어서 보내
    #응답 결과를 받는다.
    response = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text
    context = {'response': response,}
    return render(request, 'pages/result.html', context)


def user_new(request):
    return render(request, 'pages/user_new.html')


def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {
        'name': name,
        'pwd': pwd,
    }
    return render(request, 'pages/user_create.html', context)


def static_example(request):
    return render(request, 'pages/static_example.html')