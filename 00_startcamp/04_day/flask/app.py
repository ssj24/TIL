from flask import Flask, render_template, request
from datetime import datetime
import random
app = Flask(__name__)

@app.route('/')
def hello():
    # return 'Hello World!'#함수나 클래스끼리는 두 줄씩 뛰는 게 정석
    return render_template('index.html')


@app.route('/ssafy')
def ssafy():
    return 'This is SSAFY!'


@app.route('/dday')
def dday():
    #오늘 날짜
    today_time = datetime.now()
    #수료 날짜
    endgame = datetime(2019, 11, 29)
    #수료 날짜 - 오늘 날짜
    dday = endgame - today_time
    return f'{dday.days}일 남았습니다.'#.days를 하면 일수만 말해줌


@app.route('/html')
def html():
    return '<h1>This is html tag!</h1>'#html태그도 보낼 수 있음!!!!


@app.route('/html_line')
def html_line():
    return """
    <h1>여러 줄을 보내 봅시다.</h1>
    <ul>
        <li>  사과  </li>
        <li>  수박  </li>
        <li>  자두  </li>
    </ul>
    """


@app.route('/greeting/<name>')#변수 name을..<>안은 string이 기본값! 숫자를 넣으려면 int등을 써줘야함
def greeting(name):#변수를 함수 인자로 써야 인식
    # return f'반갑습니다! {name}'
    return render_template('greeting.html', html_name=name)#name변수를 html파일에 넘겨준 것(html_name)이라는 변수로! 실제로는 html로 넘어가는 변수 이름이 같아도 무관함. name=name이렇게 해도 됨

@app.route('/cube/<int:number>')
def cube(number):
    #연산을 모두 끝내고 변수만 cube.html로 넘긴다
    number2=number**3
    # return f'{number} 세제곱은 {number**3}입니다.'#제곱은 **로 표시
    return render_template('cube.html', html_number2=number2, html_number=number)#변수를 여러개 보낼 수 있음

@app.route('/lunch/<int:number>')
def lunch(number):
    # lunch_menu = ['레드코코넛누들', '시리얼', '탄산수', '견과류']
    # return f'오늘의 점심은 {random.sample(lunch_menu, number)}'
    menu = ['한우불고기', '코코넛 머시기', '도시락', '삼계탕', '볶음밥']
    boxes = []
    for i in range(number):# 얘네는 중복 가능
        boxes.insert(i,random.choice(menu))
    return f'여러분의 점심메뉴는{boxes}입니다.'


@app.route('/movie')
def movie():
    movies = ['토이스토리1', '토이스토리2', '토이스토리3', '토이스토리4', '스파이더맨', '배심원들']
    return render_template('movies.html', movies=movies)


@app.route('/ping')
def pint():
    return render_template('ping.html')


@app.route('/pong')
def pong():
    print(request.args)#이걸 보면 request가 딕셔너리임을 알 수 있음 그래서 key와 value가 필요
    whats = request.args.get('data')#넘어오는 자료의 key값!(input의 name)
    return render_template('pong.html', whats=whats)


@app.route('/naver')
def naver():
    return render_template('naver.html')
# 검색하면 네이버로 검색


@app.route('/google')
def google():
    return render_template('google.html')


@app.route('/fakevonvon')
def whor():
    return render_template('fake.html')


@app.route('/fakevonvon_2')
def recomm():
    # bev_list1 = ['아아', '그린티블렌디드', '캐모마일', '더치커피', '자몽피지오']
    # bev_list2 = ['아아', '그린티블렌디드', '캐모마일', '더치커피', '자몽피지오']
    # bev_list3 = ['아아', '그린티블렌디드', '캐모마일', '더치커피', '자몽피지오']

    # recomme1=random.choice(bev_list1)
    # recomme2=random.choice(bev_list2)
    # recomme3=random.choice(bev_list3)

    # whatsup = request.args.get('bev_')
    # return render_template('vonvon.html', whatsup=whatsup, recomme1=recomme1, recomme2=recomme2, recomme3=recomme3)
    person = ['체력', '건강', '피곤', '힘듦', '졸림' , '활기']
        choice = random.sample(person,3)
        name = request.args.get('data')
        return render_template('receive.html',choice=choice, name = name)