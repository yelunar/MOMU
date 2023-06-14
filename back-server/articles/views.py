
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment
from movies.models import Movie, Music

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    # print(request.user)
    # print(movie)
    if request.method == 'GET':
        articles = movie.movie_articles.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # print(serializer)
            serializer.save(user=request.user)
            link12(serializer.data, movie)
            # print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


def link12(data, movie):
    id = data.get('id')
    article = Article.objects.get(pk=id)
    article.article_movie.add(movie)
    # print(movie.id ,movie.title)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def music_article_list(request, music_pk):
    music = Music.objects.get(pk=music_pk)
    # print(request.user)
    # print(music)
    if request.method == 'GET':
        articles = music.music_articles.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # print(serializer)
            serializer.save(user=request.user)
            link45(serializer.data, music)
            # print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


def link45(data, music):
    id = data.get('id')
    article = Article.objects.get(pk=id)
    article.article_music.add(music)
    # print(music.id ,music.title)




@api_view(['GET', 'DELETE', 'PUT'])
# @permission_classes([IsAuthenticated])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'POST'])
def comment_list(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == "POST":
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == "GET":
        comments = article.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)



@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # print(123)
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def like_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user
    # print(user)
    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    else:
        article.like_users.add(user)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    


#############################

