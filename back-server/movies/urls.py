# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views


urlpatterns = [
    # # 배우 전체
    # path('actor/', views.actor_list),
    # # 배우 상세
    # path('actor/<int:actor_pk>/', views.actor_detail),

    # 영화 전체
    path('movies/', views.movie_list),
    # 영화 상세
    path('movie/<int:movie_pk>/', views.movie_detail),
    #영화 좋아요
    path('movie/like/<int:movie_pk>/', views.like_movie),


    path('movie/rank/like/', views.movieranklike),
    # 리뷰 많은 순
    path('movie/rank/article/', views.movierankarticle),


    
    path('movie_search/<str:movie>/', views.search_movie), 
    path('music_search/<str:musicname>/', views.search_music), 

    path('newmovie/', views.movie),

    path('genre/', views.genre),

    path('musicgenre/', views.musicgenre),

    # 음악 전체
    path('music/', views.music_list),
    # 음악 상세
    path('music/<int:music_pk>/', views.music_detail),
    # 음악 좋아요
    path('music/like/<int:music_pk>/', views.like_music),

    path('music/rank/article/', views.musicrankarticle),
    # 좋아요 많은 순
    path('music/rank/like/', views.musicranklike),
]

