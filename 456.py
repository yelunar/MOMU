# 6b60e4f315c9444da4cc0f467c248932



# http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=6b60e4f315c9444da4cc0f467c248932&itemPerPage=100


'''
directors	문자열	영화감독을 나타냅니다.
peopleNm   문자열	영화감독명을 출력합니다.
genreAlt	문자열	영화장르(전체)를 출력합니다.    (성인 영화 거르기)
movieNm	문자열	영화명(국문)을 출력합니다.
movieNmEn	문자열	영화명(영문)을 출력합니다.

'''
from bs4 import BeautifulSoup
import json
import requests
from collections import OrderedDict




key = '9944ad3462526525f315d360618d8337'
page = 1000
res = []
idx = 1

def recommendation(page):
    global idx, res
    print(123)
    URL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json'
    params = {
        "key": key,
        "itemPerPage":100,
        "curPage":page
    }
    #paras를 이용하여 여러 변수가 입력될 때 그 값을 할당할 수 있게 함
    response = requests.get(URL, params=params).json()
    lst = response['movieListResult']['movieList']
    print(123)
    for i in range(len(lst)):

        # 제거 조건 1 : 성인물인 경우
        if '성인물(에로)' in lst[i]['genreAlt']:
            continue

        data = ''
        for j in lst[i]['openDt']:
            data += j
            if len(data) == 4:
                data += '-'
            if len(data) == 7:
                data += '-'

        # 제거 조건 2 : 개봉일 없는 경우
        if data == '':
            continue

        keyword = lst[i]['movieNm']
        url = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=영화 ${keyword}'
        response = requests.get(url)

        flag = 1
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            try:
                img = soup.find('img', class_='_img').get("src")
                # print(img)
                if img[45]== '=':
                    img = img[:46]+'1200x1000'+img[53:]
                elif img[53] == '=':
                    flag = 0
                #     img = img[:54]+'1200x1000'+img[61:]
                # # print(img)
            except:
                # img = 'https://media.istockphoto.com/id/499642119/ko/%EB%B2%A1%ED%84%B0/%EC%82%AC%EC%9A%A9-%EA%B0%80%EB%8A%A5%ED%95%9C-%EC%82%AC%EC%A7%84-%EC%97%86%EC%9D%8C-%EB%98%90%EB%8A%94-%EB%AF%B8%EC%8B%B1-%EC%9D%B4%EB%AF%B8%EC%A7%80.webp?s=612x612&w=is&k=20&c=7c0_XObaB51UOyiKd0n0Vh7DYElthNtjazmmQyHvVhA='
                img = ''
            try:
                desc = soup.find('span', class_="desc _text").get_text()
            except:
                flag = 0
                
            if img == '':
                continue
            
        else : 
            print(response.status_code)

        # 제거조건 3,4 : 포스터가 없는 경우 / 오벼뷰가 없는 경우
        if flag == 0:
            continue

        temp = OrderedDict()
        temp['model'] = "movies.movie"
        temp['pk'] = idx
        idx += 1
        temp['fields'] = {
            'title':lst[i]['movieNm'],
            'genre':lst[i]['genreAlt'],
            'release_date':data,
            'poster_path':img,
            'overview' : desc
        }
        
        # print(temp)
        res.append(temp)
        # print(len(res))
    # print(123)
    # res.append(temp)


for i in range(1, page+1): 
    recommendation(i)

print(len(res))
with open("movies.json", "w", encoding="utf-8") as output:
    json.dump(res, output, ensure_ascii=False, indent="\t")
# print(res)




'''
46번째
7글자
0:46
1200x1000
53:

'''