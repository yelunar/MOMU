from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/<username>/', views.profile),
    path('follow/<username>/', views.follow),
    path('signup/', views.signup),
    path('imgchange/', views.imgchange),
    path('mbti/', views.mbti),

]