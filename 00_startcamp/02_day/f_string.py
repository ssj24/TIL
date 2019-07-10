name = '조수지'
print(f'안녕하세요, {name}입니다.')

#점심 메뉴 추천
import random
menu = ['부대찌개', '소고기', '카레']
lunch = random.choice(menu)
print(f'오늘의 점심은 {lunch}입니다.')

#로또 추천
#위에서 import random 했으니 생략
numbers = range(1,46)#range는 뒤의 숫자를 하나 더 해야 됨 45까지의 숫자하려면 1,46
#sorted(numbers)#오름차순 정렬
lotto = random.sample(numbers, 6)
print(f'오늘의 로또 당첨번호는 {sorted(lotto)}입니다.')#f-string은 {}안에서 함수 쓸 수 있음

#FYI
name = '홍길동'
print('안녕하세요, '+  name +'입니다.')#변수 name의 값이 문자열이기 때문에 가능