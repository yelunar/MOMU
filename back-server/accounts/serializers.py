from rest_framework import serializers
from django.contrib.auth import get_user_model
from articles.models import Article
from movies.models import Movie, Music
# from movies.serializers import MusicSerializer
User = get_user_model()

# 사용자 프로필에 들어가는 정보
class ProfileSerializer(serializers.ModelSerializer):

    class ArticleSerializer(serializers.ModelSerializer):
        class MovieSerializer(serializers.ModelSerializer):

            class Meta:
                model = Movie
                fields = ('title', 'pk', 'poster_path')
        
        article_movie = MovieSerializer(read_only=True, many=True)


        class MusicSerializer(serializers.ModelSerializer):

            class Meta:
                model = Music
                fields = '__all__'

        article_music = MusicSerializer(read_only=True, many=True)

        class Meta:
            model = Article
            fields = '__all__'


    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = '__all__'


    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'profile_image', 'nickname')


    class MusicSerializer(serializers.ModelSerializer):

        class Meta:
            model = Music
            fields = '__all__'


    like_articles = ArticleSerializer(many=True)
    articles = ArticleSerializer(many=True)

    like_movies = MovieSerializer(many=True)
    like_music = MusicSerializer(many=True)

    followings = UserSerializer(many=True, read_only=True,)
    followers = UserSerializer(many=True, read_only=True,)
    # followers = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = User
        # fields = ('pk')
        fields = '__all__'



# 유저 정보
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    nickname = serializers.CharField(max_length=50)
    mbti = serializers.CharField(max_length=4)
    # img = serializers.ImageField(default='default.png') 

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'nickname', 'mbti', 'profile_image')
        # read_only_fields = ('mbti', 'nickname')



# 사용자 프로필에 들어가는 정보
class MbtiSerializer(serializers.ModelSerializer):

    
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'


    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'profile_image', 'nickname')


    class MusicSerializer(serializers.ModelSerializer):
        class Meta:
            model = Music
            fields = '__all__'

    like_movies = MovieSerializer(many=True)
    like_music = MusicSerializer(many=True)


    class Meta:
        model = User
        # fields = ('pk')
        fields = '__all__'
