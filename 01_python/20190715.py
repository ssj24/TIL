print(int(3.5))

# a = 0.1 * 3
# b = 0.3

# import math
# print(math.isclose(a, b))

# print('"파일은 C:\\Windows\\Users\\내문서\\Python에 저장이 되어있습니다."\n나는 생각했다. \'cd를 써서 git bash로 들어가봐야지\'')

# n = 5
# m = 9

# print(((n*'*')+ '\n')*m)

# a = 1
# b = 4
# c = -21
# print((-b+(b**2 - 4*a*c)**(1/2))/2*a)
# print((-b-(b**2 - 4*a*c)**(1/2))/2*a)

# import requests

# url = "https://api.bithumb.com/public/ticker/btc"
# data = requests.get(url).json()['data']
# print(data)

# maxprice = int(data['max_price'])
# minprice = int(data['min_price'])
# gap = maxprice - minprice
# openingprice = int(data['opening_price'])


# if openingprice + gap > maxprice:
#     print('상승장')
# else:
#     print('하락장')

# my_str = "Life is too short, you need python"
# a = ['a', 'e', 'i', 'o', 'u']
# for i in a:
#     my_str=my_str.replace(i, '')
# print(my_str)
