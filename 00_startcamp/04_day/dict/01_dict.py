#dictionary만들기-1
lunch={
    '중국집': '02-098-7363'
}#dictionary는 중괄호, key와 value가 있음

#dictionary만들기-2
dinner=dict(중국집='234444', 일식집='03033')

#dictionary에 내용 추가하기
lunch['분식집']='031-0928-9383'#여기는 대괄호
print(lunch)

#dictionary 내용 가져오기
idol={
    'bts': {#dictionary 중첩
        '지민': 25, #dictionary는 한 줄에 하나씩 쓰는 걸 추천
        'RM': 24 
    }
}

#RM의 나이는? 길을 잘 찾는 것이 중요합니다.
idol['bts']['RM']#방법 1. 이건 없는 키 값을 주면 서버 에러
# idol.get('bts').get('RM')#방법 2.  이건 없는 키 값을 주면 none을 반환함