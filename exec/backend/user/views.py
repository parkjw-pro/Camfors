
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Campsite, Likes, Reviews
from .serializers import UserSignUpSerializer, UserLoginSerializer, LikesSerializer, ReviewsSerializer
from django.db.models import Subquery
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

@csrf_exempt
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


@csrf_exempt
@api_view(['post'])
@permission_classes((permissions.AllowAny,))
def like(request):
    like_query_sets = Campsite.objects.filter(campsite_id__in=Subquery(Likes.objects
                                                                      .filter(user_id=request.data['user_id'])
                                                                      .values('campsite_id')))
    like = LikesSerializer(like_query_sets, many=True)
    return JsonResponse(like.data, safe=False, status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['post'])
@permission_classes((permissions.AllowAny,))
def review(request):
    review_query_sets = Reviews.objects.filter(user_id=request.data['user_id']).order_by('-created_at')
    review = ReviewsSerializer(review_query_sets, many=True)
    return JsonResponse(review.data, safe=False, status=status.HTTP_201_CREATED)
