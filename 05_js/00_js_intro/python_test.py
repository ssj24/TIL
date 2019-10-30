# 파이썬의 익명함수 lambda
def ssafy1(x):
    return x + 1

lambda x: x + 1 # lambda 매개변수: return식
ssafy2 = lambda x: x + 1
ssafy2(2)


print(list(map(ssafy1, [1, 2, 3])))
# [2, 3, 4]
# 이걸 람다로 쓰면
print(list(map(lambda x: x + 1, [1, 2, 3])))