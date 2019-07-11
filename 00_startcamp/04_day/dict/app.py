import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')


@app.route('/lotto_result')
def lotto_result():
    #회차 번호를 받아온다.
    num = request.args.get('num')
    #동행복권에 요청을 보내 응답을 받는다.
    res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}')
    lotto = res.json()#chrome의 json viewer같은.. json은 내장함수로 json형태로 바꿔주는 것

    #당첨번호 6개만 가져오기
    winner = []
    for i in range(1, 7):
        winner.append(lotto[f'drwtNo{i}'])

    #내 번호 리스트 만들기
    numbers=[]
    for num in request.args.get('numbers').split():
        numbers.append(int(num))
    #등수 가리기(몇 개 맞았는지 교집합 찾기)
    matched = 0
    for num in numbers:
        if num in winner:#num이 winner에 있는지 판단하는 것
            matched += 1
    if matched == 6:
        result = '1등입니다!'
    elif matched == 5:
        if lotto['bnusNo'] in num:
            result = '2등입니다!'
        else:
            result = '3등입니다!'
    elif matched == 4:
        result = '4등입니다!'
    elif matched == 3:
        result = '5등입니다!'
    else:
        result = '꽝입니다!'
    return render_template('lotto_result.html', winner=winner, numbers=numbers, result=result)