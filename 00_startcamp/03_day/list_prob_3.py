'''
문제 3.
숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.
'''

number = int(input('숫자를 입력하세요: '))

# 아래에 코드를 작성해 주세요.
# if number%2 == 0:
#     print('짝수')
# else:
#     print('홀수')

#보통 true는 1이나 2,3 등 다른 값, false는 0을 인식하므로 그걸 이용해서 식을 짤 수 있음
if number%2:
    print('홀수')
else:
    print('짝수')