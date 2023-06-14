from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import ProfileSerializer, UserSerializer, MbtiSerializer
from rest_framework import status
# Create your views here.
from django.contrib.auth.hashers import check_password


from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import random

User = get_user_model()

@api_view(['GET', 'DELETE'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'GET':
        serializer = ProfileSerializer(user)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        # print(user)
        # print(request.user)
        user.pk = request.user.pk
        request.user.delete()
        return Response({ 'delete': f'{user.pk}번 회원이 탈퇴했습니다.' }, status=status.HTTP_204_NO_CONTENT)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, username):
    me = request.user
    person = get_object_or_404(get_user_model(), username=username)
    if me != person:
        if me.followings.filter(pk=person.pk).exists():
            me.followings.remove(person)
            following = False
        else:
            me.followings.add(person)
            following = True
        serializer = ProfileSerializer(person)
        # print(serializer.data)
        return Response(following)
    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST', 'PUT'])
@permission_classes([AllowAny])
def signup(request):

    if request.method == 'POST':
        # print(1)
        # print(request)
        password = request.data.get('password')
        password_confirmation = request.data.get('passwordConfirmation')

        if password != password_confirmation:
            return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=request.data.get('username')).exists():
            return Response({'error': '일치하는 이메일이 존재합니다.'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=request.data.get('nickname')).exists():
            return Response({'error': '일치하는 닉네임이 존재합니다.'}, status=status.HTTP_400_BAD_REQUEST)


        serializer = UserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()

            user.set_password(request.data.get('password'))
            user.save()
            # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다. (write_only)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method == 'PUT':

        # print(request.data)
 
        currentuser = request.data.get('currentuser')
        id = currentuser.get('id')
        originpassword = request.data.get('originpassword')
        password = request.data.get('password')
        password_confirmation = request.data.get('passwordConfirmation')
        nickname = request.data.get('nickname')
        mbti = request.data.get('mbti')
        user = get_object_or_404(User, pk=id)
        if user.check_password(originpassword):

            if password != password_confirmation:
                return Response({'error': '새 비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
            if User.objects.filter(email=request.data.get('nickname')).exists():
                return Response({'error': '일치하는 닉네임이 존재합니다.'}, status=status.HTTP_400_BAD_REQUEST)

            user.nickname = nickname
            user.mbti = mbti
            user.set_password(request.data.get('password'))
            user.save()
            return Response(status=status.HTTP_201_CREATED)
       
       
        else:
            return Response({'error': '현재 비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
       



@api_view(['POST', 'PUT'])
@method_decorator(csrf_exempt, name='dispatch')
@permission_classes([IsAuthenticated])
def imgchange(request):
    print(123)
    userpk = request.data.get('userpk')
    # print(userpk)
    img = request.data.get('profile_image')
    # print(img)
    user = get_object_or_404(User, pk=userpk)
    # img = img.decode('utf16')
    user.profile_image = img
    user.save()
    
    data = [{'profile_image': user.profile_image}]
    return Response({'data':'사진 교체 완료'})





@api_view(['POST'])
def mbti(request):
    mbti = request.data.get('mbti')
    # print(mbti)
    # mbti = 'ENFP'
    user = get_list_or_404(User)
    # lst = []
    lst12 = []
    for i in user:
        if i.mbti == mbti:
            lst12.append(i)
            # lst.append(i.like_movies)
    
    # Serializer = UserSer
    # ializer(lst)
    # print(lst12[0].username)
    # print(Serializer.data)
    serializer = MbtiSerializer(lst12, many=True)
    # print(serializer.data)
    lst = []
    lst1 = []
    for i in serializer.data:
        temp = i.get('like_movies')
        temp1 = i.get('like_music')
        for j in temp:
            if j not in lst:
                lst.append(j)
        for j in temp1:
            if j not in lst1:
                lst1.append(j)


    if len(lst) >=10:
        movie = random.sample(lst, 10)
    else:
        movie = lst


    if len(lst1) >=10:
        music = random.sample(lst1, 10)
    else:
        music = lst1

    return Response([movie, music])



