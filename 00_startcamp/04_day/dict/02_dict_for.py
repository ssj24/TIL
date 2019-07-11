#딕셔너리 반복문 활용하기

lunch={
    '중국집': '02-098-7363',
    '분식집': '03-2202-0303',
    '일식집': '04-202-1101'
}

#기본 활용
for key in lunch:
    print(key)
    print(lunch[key])

#.items()
for key, value in lunch.items():#key와 value는 그냥 아무거나 써도 됨 like i
    print(key, value)

#value만 가져오기
for value in lunch.values():
    print(value)

#key만 가져오기
for key in lunch.keys():
    print(key)