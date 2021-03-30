from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .serializers import UserSerializer
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework import status
import jwt
# jsonparser로 requset body 데이터 얻을수 있음

ALGORITHM = "HS256"
KEY = "304!!"

# 서비스 단위 하나
@csrf_exempt
@api_view(['post'])
@permission_classes((permissions.AllowAny,))
def signup(request):
    if request.method == 'POST':
        print("post method")
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            print("not valid")
            return JsonResponse(status=status.HTTP_406_NOT_ACCEPTABLE)
        if User.objects.filter(email = request.data['email']).exists():
            print("already")
            return JsonResponse("이미 회원 가입된 회원입니다..", safe=False, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            print("save")
            serializer.save()
            return JsonResponse("회원 가입 완료.", safe=False, status=status.HTTP_201_CREATED)

def delete(request, email):
    if not User.objects.filter(email = email).exists():
        return JsonResponse(status=status.HTTP_406_NOT_ACCEPTABLE)
    user = User.objects.get(email=email)
    user.delete()
    return JsonResponse("삭제 성공", safe=False, status=status.HTTP_201_CREATED)

@csrf_exempt
@api_view(['post'])
@permission_classes((permissions.AllowAny,))
def login(request):
    if User.objects.filter(email = request.data['email'], password = request.data['password']).exists():
        token = jwt.encode({'email' : request.data['email']}, KEY, ALGORITHM)
        # request.session['email'] = request.data['email']
        return JsonResponse([request.data['email'], token], safe=False, status=status.HTTP_201_CREATED)
    return JsonResponse("로그인 실패", safe=False, status=status.HTTP_406_NOT_ACCEPTABLE)

def logout(request):
    # request.session.clear()
    return JsonResponse("로그아웃 성공", safe=False, status=status.HTTP_201_CREATED)

def session(request):
    if request.session['email']:
        user = User.objects.filter(email = request.session['email'])
        return user.email
    return JsonResponse("로그인을 해주세요", safe=False, status=status.HTTP_406_NOT_ACCEPTABLE)

