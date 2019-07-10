import requests
from bs4 import BeautifulSoup

#bs4전체가 필요하면 import bs4해도 됨 다만 이 때, BeautifulSoup을 쓰려면 soup = bs4.BeautifulSoup()처럼 매번 같이 써줘야합니다.

url = 'https://www.naver.com'

#요청 보내서 html 파일 받고
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
keywords = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a')

#뷰숲으로 정제

#select 메서드로 사용해서 list를 얻어낸다


#뽑은 list를 with구문으로 잘 작성해보자(txt파일로 작성)
# with open('example.txt', 'w', encoding='utf-8') as f:#한글 깨지니까 인코딩
#     for keyword in keywords:
#         f.write(f'{keyword.text}\n')


#랭크를 같이 따려면~?#soup.select에서 a.ah_k를 a만 남긴다
with open('example.txt', 'w', encoding='utf-8') as f:#한글 깨지니까 인코딩
    for keyword in keywords:
        rank = keyword.select_one('span.ah_r').text
        keyword = keyword.select_one('span.ah_k').text
        f.write(f'{rank}위: {keyword}\n')