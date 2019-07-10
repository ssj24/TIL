operand1, operator, operand2 = 0, "", 0

operand1 = int(input("첫 번째 숫자를 입력하세요: "))
operator = input("연산자를 입력하세요 (+, -, *, /): ")
operand2 = int(input("두 번째 숫자를 입력하세요: "))

if operator == "+":
    print("%d + %d = %d" % (operand1, operand2, operand1+operand2))
elif operator == "-":
    print("%d - %d = %d" % (operand1, operand2, operand1-operand2))
elif operator == "*":
    print("%d * %d = %d" % (operand1, operand2, operand1*operand2))
elif operator == "/":
    print("%d / %d = %.2f" % (operand1, operand2, operand1/operand2))  
else:
    print("'%s'는 본 프로그램에서 지원하지 않는 연산자입니다" % operator) 