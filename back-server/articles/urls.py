# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views


urlpatterns = [
    path('<int:movie_pk>/movie_articles/', views.article_list),
    path('<int:music_pk>/music_articles/', views.music_article_list),

    path('articles/<int:article_pk>/', views.article_detail),


    path('like/<int:article_pk>/', views.like_article),
    path('articles/<int:article_pk>/comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    


    # path('articles/<int:article_pk>/comments/', views.comment_create),
    # # 필수 작성
    # path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # optional UI
]
