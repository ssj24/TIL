import requests
from bs4 import BeautifulSoup

# 1. 원하는 주소로 요청을 보내 응답을 저장한다.
html = requests.get('https://finance.naver.com/sise/').text
soup = BeautifulSoup(html, 'html.parser')#html을 html.parser로 바꿈
# print(type(soup))
# print(type(html))
kospi = soup.select_one('#KOSPI_now').text#개발자도구에서 copy-copy selector    뒤에 .text를 붙이면 텍스트만 나옴
print(kospi)