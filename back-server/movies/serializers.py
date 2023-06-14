from rest_framework import serializers 
from .models import Movie, Music  # Actor,
from articles.serializers import CommentSerializer
from django.contrib.auth import get_user_model
from articles.models import Article, Comment

User = get_user_model()

# 영화의 제목만
class TitleSerializer(serializers.ModelSerializer):
    movie_count = serializers.IntegerField(source='movie_articles.count', read_only=True)
    like_count = serializers.IntegerField(source='like_users.count', read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'genre', 'like_count','movie_count' )




class ArticleSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'nickname')
            read_olny_fields = ('nickname',)


    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'
            # read_olny_fields = ('',)

    movie = MovieSerializer(read_only=True)


    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    like_users = UserSerializer(read_only=True, many=True)

    like_count = serializers.IntegerField(source='like_users.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'username', 'comment_set', 'comment_count', 'movie')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'nickname')
        read_olny_fields = ('nickname',)


# 영화 전체
class MovieSerializer(serializers.ModelSerializer):

    # review_set = ReviewsSerializer(many=True)
    username = serializers.CharField(source='user.username', read_only=True)
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    like_users = UserSerializer(read_only=True, many=True)
    like_count = serializers.IntegerField(source='like_users.count', read_only=True)
    
    movie_articles = ArticleSerializer(many=True, read_only=True)
    movie_count = serializers.IntegerField(source='movie_articles.count', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('user', 'username',)


class MovieSearchSerializer(serializers.ModelSerializer):

    similarity = serializers.FloatField(default=0)

    class Meta:
        model = Movie
        fields = ('pk', 'title', 'poster_path', 'similarity', 'overview', 'genre')




# 뮤직
class MusicSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.username', read_only=True)
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    like_users = UserSerializer(read_only=True, many=True)
    like_count = serializers.IntegerField(source='like_users.count', read_only=True)
    
    music_articles = ArticleSerializer(many=True, read_only=True)
    music_count = serializers.IntegerField(source='music_articles.count', read_only=True)

    class Meta:
        model = Music
        fields = '__all__'





class MovieLikeSerializer(serializers.ModelSerializer):
    like_users = UserSerializer(read_only=True, many=True)
    like_count = serializers.IntegerField(source='like_users.count', read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'like_count', 'like_users')

class MoviearticleSerializer(serializers.ModelSerializer):
      
    movie_articles = ArticleSerializer(many=True, read_only=True)
    movie_count = serializers.IntegerField(source='movie_articles.count', read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'movie_articles', 'movie_count')




class NewMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'release_date' ,'overview', 'genre' )
