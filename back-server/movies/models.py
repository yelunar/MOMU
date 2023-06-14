# Create your models here.
from django.db import models
from django.conf import settings
# Create your models here.
# class Actor(models.Model):
#     name = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    release_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    poster_path = models.TextField()
    overview = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    
    
    # movie와 actor을 n대n 관계로 설정
    # actors = models.ManyToManyField(Actor,related_name="movies")


# class Review(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     # movie를 review의 외래키로 설정
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    album_img = models.TextField()
    genre = models.CharField(max_length=100)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_music')