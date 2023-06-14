from bs4 import BeautifulSoup
import requests

URL = 'https://movie.daum.net/ranking/boxoffice/yearly'
# params = {
#     "q":'아프리카모의법정'
# }

# response = requests.get(URL, params=params)
response = requests.get(URL)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    name = soup.find('a', class_="link_txt").get_text()
    print(name)
else : 
    print(response.status_code)



'''
장르나 태그로 음악선정 > 리스트 만들기
>
이걸 바탕으로 크롤링해서 데이터 뽑기 > 가수, 노래, 앨범이미지 
음악 모델 > article이랑 연결, 유저랑 연결, 시리얼라이져 설정
추천 영화 & 음악 >> 영화는 디테일로 넘기기 / 음악은 음악 틀면서 정보 주기



'''