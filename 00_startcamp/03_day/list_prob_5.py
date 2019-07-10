'''
문제 5.
표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.
# 입력 예시: 300000;20000;10000
'''

prices = input('물품 가격을 입력하세요: ')

# 아래에 코드를 작성해 주세요.
prices_list = prices.split(';')
# print(type(prices_list))

boxes = []#빈 리스트 생성, 문자열 기반의 prices_list를 숫자로 바꿔 저장
for price in prices_list:
    boxes.append(int(price))#list에 요소를 추가하는 메서드 .append()
print(boxes)

boxes.sort(reverse=True)#얘는 맨 앞자리만 봐서 90이 400앞에 옴...그렇다면 숫자로 형변환을 해 주자

# print(prices_list)
for box in boxes:
    print(box)