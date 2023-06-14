from django.db import models
from django.contrib.auth.models import AbstractUser




# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    nickname = models.CharField(max_length=50)
    mbti = models.CharField(max_length=4, blank=True)
    profile_image = models.ImageField(default='default.png')