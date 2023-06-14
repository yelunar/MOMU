from bs4 import BeautifulSoup
import json
import requests
from collections import OrderedDict

URL = 'https://music.bugs.co.kr/chart'
# params = {
#     "q":'아프리카모의법정'
# }

# response = requests.get(URL, params=params)
response = requests.get(URL)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)

    lst2 = []
    album_img = soup.find_all('a', class_="thumbnail") 
    # print(album_img)
    
    try:
        for i in album_img:
            if i.find('img'):
                lst2.append(i.find('img').get('src'))
    except:
        pass       
        
    lst3 = []
    title = soup.find_all('p', class_="title")
    # print(title)
    try:
        for i in title:
            lst3.append(i.get_text().strip())
    except:
        pass
    
    lst4 = []
    artist = soup.find_all('p', class_="artist")
    try:
        for i in artist:
            lst4.append(i.get_text().strip())
    except:
        pass
  
    album = soup.find_all('td', class_="left")
    lst = []
    try:
        for i in album:
            if i.find('a', class_='album'):
                lst.append(i.find('a', class_='album').get_text())
    except:
        pass

else : 
    print(response.status_code)

res = []
idx = 1
# print(len(lst))
# print(len(lst2))
# print(len(lst3))
# print(len(lst4))

for i in range(100):

    temp = OrderedDict()
    temp['model'] = "musics.music"
    temp['pk'] = idx
    temp['fields'] = {
        'title':lst3[idx-1],
        'artist':lst4[idx-1],
        'album':lst[idx-1],
        'album_img':lst2[idx-1]
    }
    idx += 1
    res.append(temp)
    
# print(len(res))
with open("music.json", "w", encoding="utf-8") as output:
    json.dump(res, output, ensure_ascii=False, indent="\t")
print(res)




'''
장르나 태그로 음악선정 > 리스트 만들기
>
이걸 바탕으로 크롤링해서 데이터 뽑기 > 가수, 노래, 앨범이미지 
음악 모델 > article이랑 연결, 유저랑 연결, 시리얼라이져 설정
추천 영화 & 음악 >> 영화는 디테일로 넘기기 / 음악은 음악 틀면서 정보 주기



'''