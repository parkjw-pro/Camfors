from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .serializers import UserSignUpSerializer
from .serializers import UserLoginSerializer
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
        serializer = UserSignUpSerializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse(status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            serializer.save()
            return JsonResponse("회원 가입 완료.", safe=False, status=status.HTTP_201_CREATED)

@csrf_exempt
@api_view(['post'])
@permission_classes((permissions.AllowAny,))
def checkEmail(request):
    if User.objects.filter(email = request.data['email']).exists():
        return JsonResponse("회원 가입된 이메일입니다.", safe=False, status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        return JsonResponse("가입 가능한 이메일입니다.", safe=False, status=status.HTTP_201_CREATED)

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
    user = User.objects.filter(email = request.data['email'], password = request.data['password'])
    serializer = UserLoginSerializer(user, many = True)
    if user.exists():
        token = jwt.encode({'email' : request.data['email']}, KEY, ALGORITHM)
        return JsonResponse([serializer.data, token], safe=False, status=status.HTTP_201_CREATED)
    return JsonResponse("로그인 실패", safe=False, status=status.HTTP_406_NOT_ACCEPTABLE)

def logout(request):
    return JsonResponse("로그아웃 성공", safe=False, status=status.HTTP_201_CREATED)

