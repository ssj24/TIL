import requests
from bs4 import BeautifulSoup
html = requests.get('https://www.naver.com/').text
soup = BeautifulSoup(html, 'html.parser')
keywords = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a .ah_k')
#경로를 잘 정제해줘야 합니당 #select_one 이 아니라 #select!
for i in keywords:
    print(i.text)#.text를 안 붙이면 html태그가 다 나옴

#두번째 commit을 위한 주석