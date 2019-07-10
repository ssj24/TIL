'''
문제 2.
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
'''

numbers = int(input('숫자를 입력하세요: ')) #input 이라 string으로 넘어오니까 그걸 int로 바꿔준 것

# 아래에 코드를 작성해 주세요.
for i in range(numbers):
    print(i+1)#0부터 실행되기 때문