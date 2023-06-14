from bs4 import BeautifulSoup
import json
import requests
from collections import OrderedDict

URL = 'https://movie.daum.net/ranking/boxoffice/weekly'
# params = {
#     "q":'아프리카모의법정'
# }

# response = requests.get(URL, params=params)
response = requests.get(URL)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)

    lst1 = []  # poster_img
    poster_img = soup.find_all('div', class_="poster_movie")

    try:
        for i in poster_img:
            if i.find('img'):
                lst1.append(i.find('img').get('src'))
    except:
        pass

    lst2 = []
    title = soup.find_all('strong', class_="tit_item")
    # print(title)
    try:
        for i in title:
            lst2.append(i.get_text())
    except:
        pass

    lst3 = []
    movie_date = soup.find_all('span', class_="txt_num")
    try:
        for i in movie_date:
            lst3.append(i.get_text())
    except:
        pass

    lst4 = []
    people_num = soup.find_all('span', class_="info_txt")

    try:
        for i in people_num:
            if i.get_text()[0] == '관':
                lst4.append(i.get_text()[3:])

    except:
        pass

else:
    print(response.status_code)

res = []
idx = 1

for i in range(14):

    temp = OrderedDict()
    temp['model'] = "movies.movie"
    temp['pk'] = idx
    temp['fields'] = {
        'title': lst2[idx-1],
        'movie_date': lst3[idx-1],
        'people_num': lst4[idx-1],
        'poster_img': lst1[idx-1]
    }
    idx += 1
    res.append(temp)

print(len(res))
with open("123.json", "w", encoding="utf-8") as output:
    json.dump(res, output, ensure_ascii=False, indent="\t")
print(res)
