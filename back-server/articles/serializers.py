from rest_framework import serializers
from .models import Article, Comment
from movies.models import Movie, Music
from django.contrib.auth import get_user_model
User = get_user_model()

class ArticleListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'nickname')
            read_olny_fields = ('nickname',)

    user = UserSerializer(read_only=True)
    # comment_count = serializers.IntegerField()    # query annotate로 view에서 채워줄 것!
    # like_count = serializers.IntegerField()


    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'
            # read_olny_fields = ('',)

    movie = MovieSerializer(read_only=True, many=True)


    class Meta:
        model = Article
        # fields = ('id', 'title', 'content')
        fields = ('id', 'title', 'content', 'user', 'username', 'movie')



class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    nickname = serializers.CharField(source='user.nickname', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article', 'user', 'username')



class ArticleSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'nickname')
            read_olny_fields = ('nickname',)


    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('__all__')
            # read_olny_fields = ('title')

    class MusicSerializer(serializers.ModelSerializer):
        class Meta:
            model = Music
            fields = ('__all__')

    article_movie = MovieSerializer(read_only=True, many=True)

    article_music = MusicSerializer(read_only=True, many=True)

    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    
    username = serializers.CharField(source='user.username', read_only=True)
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    
    like_users = UserSerializer(read_only=True, many=True)
    like_count = serializers.IntegerField(source='like_users.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'username', 'comment_set', 'comment_count')
