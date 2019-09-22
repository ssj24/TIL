import requests
from pprint import pprint
from faker import Faker#외부 라이브러리니까 맨 위로
from decouple import config
from django.shortcuts import render
from .models import Job

# Create your views here.
def index(request):
    return render(request, 'jobs/index.html')


def past_life(request):
    #사용자로부터 이름 데이터를 받음
    if request.method == 'POST':
        name = request.POST.get('name')
        #db에 매칭되는 name 가져오기
        # Job.objects.get(name=name)#이건 없으면 오류남
        person = Job.objects.filter(name=name).first()#비어 있으면 무조건 첫번째 값을 가져와라
        
        # db에 person이 있는지 없는지 판단
        if person:# db에 기존 이름이 있다면
            past_job = person.past_job
        else: # db에 기존 이름이 없다면(person이 빈 쿼리셋(==False))
            faker = Faker()
            past_job = faker.job()
            person = Job(name=name, past_job=past_job) #새로운 레코드를 추가한다.
            person.save()

        #GIPHY (past_job을 API에 요청을 보내서 응답을 받음)
        GIPHY_API_KEY = config('GIPHY_API_KEY')
        url = f'http://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={past_job}&limit=1'
        # pprint(requests.get(url).json())
        data = requests.get(url).json()
        try: # image가 없을 때 에러처리하려구
            image = data.get('data')[0].get('images').get('original').get('url')
        except IndexError:
            image = None

        context = {'person': person, 'image': image,}
        return render(request, 'jobs/past_life.html', context)      

