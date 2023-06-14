from django.shortcuts import render
from .models import  Movie, Music
from .serializers import  MovieSerializer, MovieSearchSerializer, NewMovieSerializer, MoviearticleSerializer, MovieLikeSerializer, MusicSerializer, TitleSerializer
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import random

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from jellyfish import jaro_winkler_similarity

from bs4 import BeautifulSoup
import requests

from django.db.models import Q


allgenre = ['다큐멘터리', '코미디', '가족', '미스터리',
             '멜로/로맨스', '스릴러', '어드벤처', '기타', '서부극(웨스턴)',
               '전쟁', '판타지', 'SF', '액션', '공연', '뮤지컬',
                 '사극', '범죄', '드라마', '공포(호러)', '애니메이션']


# 영화 전체
@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializers = TitleSerializer(movies, many=True)
    # data = random.sample(serializers.data, 100)
    return Response(serializers.data)

# 영화 상세
@api_view(['GET'])
def movie_detail(request, movie_pk):
    # print(123)
    # print(movie_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    # print(movie)
    movie = Movie.objects.get(pk=movie_pk)
    serializer = MovieSerializer(movie)
    
    return Response(serializer.data)



@api_view(['POST'])
def like_movie(request, movie_pk):
    user = request.user
    # print(user)
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.like_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def music_list(request):
    musics = get_list_or_404(Music)
    serializers = MusicSerializer(musics, many=True)
    return Response(serializers.data)

# 영화 상세
@api_view(['GET'])
def music_detail(request, music_pk):
    # print(123)
    music = get_object_or_404(Music, pk=music_pk)
    music = Music.objects.get(pk=music_pk)
    serializer = MusicSerializer(music)
    
    return Response(serializer.data)


@api_view(['POST'])
def like_music(request, music_pk):
    user = request.user
    # print(user)
    music = get_object_or_404(Music, pk=music_pk)
    if music.like_users.filter(pk=user.pk).exists():
        music.like_users.remove(user)
        serializer = MusicSerializer(music)
        return Response(serializer.data)
    else:
        music.like_users.add(user)
        serializer = MusicSerializer(music)
        return Response(serializer.data)
    

@api_view(['GET'])
def search_movie(request, movie):
    # print(movie)
    movies = get_list_or_404(Movie)
    # print(movies)
    serializer = MovieSearchSerializer(movies, many=True)   
    lst = []
    for data in serializer.data:
        temp = {'pk': 0, 'title': '', 'poster_path':'', 'similarity':''}
        temp['pk'] = data['pk']; temp['title'] = data['title']; temp['poster_path'] = data['poster_path']
        temp['similarity'] = jaro_winkler_similarity(movie, data['title'])
        lst.append(temp)
    lst.sort(key=lambda x : -x['similarity'])
    serializer = lst[:10]
    return Response(serializer)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def search_movie(request, movie):
#     movies = get_list_or_404(Movie.objects.filter(Q(title__icontains=movie)))
#     serializer = MovieSerializer(movies, many=True)
#     return Response(serializer.data)



@api_view(['GET'])
def search_music(request, musicname):
    # print(musicname)
    music = get_list_or_404(Music)
    # print(movies)
    serializer = MusicSerializer(music, many=True)   
    musiclst = []
    for data in serializer.data:
        tmp = {'id': 0, 'title': '', 'album_img':'', 'similarity':''}
        tmp['id'] = data['id']; tmp['title'] = data['title']; tmp['album_img'] = data['album_img']
        tmp['similarity'] = jaro_winkler_similarity(musicname, data['title'])
        musiclst.append(tmp)
    musiclst.sort(key=lambda x : -x['similarity'])
    serializer = musiclst[:5]
    return Response(serializer)




@api_view(['POST'])
def genre(request):
    # print(request.data)
    check = request.data.get('genre')
    # print(check)
    movies = get_list_or_404(Movie)
    serializer = MovieSearchSerializer(movies, many=True)
    lst1 = []
    for data in serializer.data:
        for i in check:
            if i in data['genre']:
                lst1.append(data)
    # print(lst1)
    # print(len(lst1))
    data = random.sample(lst1, 10)
    return Response(data)


@api_view(['POST'])
def musicgenre(request):
    # print(request.data)
    check = request.data.get('genre')
    # print(check)
    music = get_list_or_404(Music)
    serializer = MusicSerializer(music, many=True)
    lst1 = []
    for data in serializer.data:
        for i in check:
            if i in data['genre']:
                lst1.append(data)
    # print(lst1)
    # print(len(lst1))
    if len(lst1) > 10:
        data = random.sample(lst1, 10)
    else:
        data = lst1
    return Response(data)




@api_view(['GET'])
def musicrankarticle(requset):
    music = Music.objects.all().order_by('-music_articles')
    lst = []
    for i in music:
        if i not in lst:
            lst.append(i)
        if len(lst)==10:
            break
    serializer = MusicSerializer(lst, many=True)
    lst = sorted(serializer.data, key=lambda x : -x['music_count'])
    return Response(lst)
    


@api_view(['GET'])
def musicranklike(request):
    music = Music.objects.all().order_by('-like_users')
    lst12 = []
    for i in music:
        if i not in lst12:
            lst12.append(i)
        if len(lst12)==10:
            break
    serializer = MusicSerializer(lst12, many=True)
    lst12 = sorted(serializer.data, key=lambda x : -x['like_count'])
    return Response(lst12)


@api_view(['GET'])
def movierankarticle(requset):
    movie = Movie.objects.all().order_by('-movie_articles')
    lst12 = []
    for i in movie:
        if i not in lst12:
            lst12.append(i)
        if len(lst12)==10:
            break
    serializer = MoviearticleSerializer(lst12, many=True)
    lst12 = sorted(serializer.data, key=lambda x : -x['movie_count'])
    # print(lst12)
    return Response(lst12)


@api_view(['GET'])
def movieranklike(request):
    movie = Movie.objects.all().order_by('-like_users')
    lst = []
    for i in movie:
        if i not in lst:
            lst.append(i)
        if len(lst)==10:
            break
    serializer = MovieLikeSerializer(lst, many=True)
    lst = sorted(serializer.data, key=lambda x : -x['like_count'])
    # print(serializer.data)
    return Response(lst)




@api_view(['GET'])
@permission_classes([AllowAny])
def movie(request):
    URL = 'https://movie.daum.net/ranking/boxoffice/weekly'

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

    data = []
    idx = 1
    pkn = 14919
    for i in range(15):

        temp = {}
        temp['pk']=pkn,
        pkn += 1
        temp['title']= lst2[idx-1],
        temp['release_date']= lst3[idx-1],
        temp['people_num']= lst4[idx-1],
        temp['poster_path']= lst1[idx-1]
        temp['overview']=''
        temp['genre']=''
        
        idx += 1
        data.append(temp)
        # add(temp)
    # print(data)
    return Response(data)

