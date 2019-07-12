import requests
from decouple import config
from flask import Flask, render_template, request

app = Flask(__name__)


api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')


@app.route('/')
def hello():
    return 'Hi there!'


# @app.route('/write')
# def write():
#     return render_template('write.html')


# @app.route('/send')
# def send():
#     text = request.args.get('message')
    
#     requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
#     return render_template('send.html')


@app.route(f'/{token}', methods=['POST'])#아무 요청이나 받지 않기 위해 토큰을 넣어줌#요청을 해야 답이 옴
def telegram():
    #step 1. 데이터 구조 print해보기
    # print(request.get_json())
    from_telegram = request.get_json()

    if from_telegram.get('message') is not None:#메세지가 비어 있지 않을 때만 step2 진행하라는 것
        #step 2. 그대로 돌려보내기
        chat_id = from_telegram.get('message').get('from').get('id')
        text = from_telegram.get('message').get('text')
        # 한글 키워드 받기 but 메아리와 다른 조건이 필요
        
        #번역으로 입력이 싲가된다면, 파파고로 동작이 시작된다.
        if text[0:4] == '/한영 ': #/번역 그리고 띄워쓰기까지 4글자라서 슬라이스는 0~4의 5개
            headers = {
                'X-Naver-Client-Id': naver_client_id,
                'X-Naver-Client-Secret': naver_client_secret
            }
            data = {'source': 'ko', 'target': 'en', 'text': text[4:] }#data = "source=ko&target=en&text=" + encText 이걸 딕셔너리로
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)#requests.args.get은 받아올 때. 이건 요청 보내는 거라 없음 .get하면 다 보여서 .post로
            # print(papago_res.json())       
            text = papago_res.json().get('message').get('result').get('translatedText')#여기에 한영번역텍스트가 있다. 
        
        # requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')#이게 두 줄 되면 메아리가 쳐요

        if text[0:5] == '/enk ': #/번역 그리고 띄워쓰기까지 4글자라서 슬라이스는 0~4의 5개
            headers = {
                'X-Naver-Client-Id': naver_client_id,
                'X-Naver-Client-Secret': naver_client_secret
            }
            data = {'source': 'en', 'target': 'ko', 'text': text[4:] }#data = "source=ko&target=en&text=" + encText 이걸 딕셔너리로
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)#requests.args.get은 받아올 때. 이건 요청 보내는 거라 없음 .get하면 다 보여서 .post로
            # print(papago_res.json())       
            text = papago_res.json().get('message').get('result').get('translatedText')#여기에 한영번역텍스트가 있다. 
        

        if text[0:4] == '/로또 ':  
            num = text[4:]#회차 번호를 받아온다.4번째 이후의 입력값
            
            #동행복권에 요청을 보내 응답을 받는다.
            res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}')#원래 common.do앞에 token값을 넣어야 반환해주는데 동행복권은 착하넹
            lotto = res.json()#chrome의 json viewer같은.. json은 내장함수로 json형태로 바꿔주는 것

            #당첨번호 6개만 가져오기
            winner = []
            for i in range(1, 7):
                winner.append(lotto[f'drwtNo{i}'])
            bonus_num = lotto['bnusNo']
            text = f'로또 {num}회차의 당첨 번호는 {winner}입니다. 보너스 번호는 {bonus_num}입니다.'
        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    return '', 200#무조건 200을 받아야 해서


    
  


