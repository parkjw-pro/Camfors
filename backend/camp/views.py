from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Subquery
import json
from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework import status
from .models import Campsite, CampsiteTag, Tag, Reviews
from .serializers import CampsiteSerializer, CampsiteDetailSerializer, TagSerializer, CampCreateReviewSerializer, CampReadReviewSerializer
# jsonparser로 requset body 데이터 얻을수 있음


# 서비스 단위 하나
def campSite_list(request):
    if request.method == 'GET':
        query_sets = Campsite.objects.all()
        serializer = CampsiteSerializer(query_sets, many=True)
        return JsonResponse(serializer.data, safe=False)


def campSite_detail(request, pk):
    try:
        campsite = Campsite.objects.get(pk=pk)
    except Campsite.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CampsiteDetailSerializer(campsite)
        return JsonResponse(serializer.data, safe=False)


def camptaglist(request, tag_id):
    try:
        query_sets = Campsite.objects.filter(campsite_id__in=Subquery(CampsiteTag.objects
                                                                      .filter(tag_id=tag_id)
                                                                      .values('campsite_id'))).order_by('likeCount')[:20]
    except Campsite.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET' and len(query_sets) > 0:
        serializer = CampsiteSerializer(query_sets, many=True)
        return JsonResponse(serializer.data, safe=False)

    else:
        return JsonResponse("조회된 데이터가 없습니다.", safe=False)


def campLikesList(request):
    try:
        query_sets = Campsite.objects.all().order_by('-likeCount')[:20]
    except Campsite.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET' and len(query_sets) > 0:
        serializer = CampsiteSerializer(query_sets, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def campWordResult(request):
    if request.method == 'POST':
        try:
            word = json.loads(request.body)
            searchword = word.get('word')
            query = Campsite.objects.filter(Q(campsite_name__icontains=searchword) | Q(addr1__icontains=searchword) |
                                    Q(indutyV__icontains=searchword) | Q(glampInnerFclty__icontains=searchword) |
                                            Q(posblFcltyCl__icontains=searchword) | Q(exprnProgrm__icontains=searchword) |
                                            Q(themaEnvrnCl__icontains=searchword) | Q(eqpmnLendCl__icontains=searchword)).distinct()

            result=CampsiteSerializer(query,many=True)

        except Campsite.DoesNotExist:
            return HttpResponse(status=404)

    return JsonResponse(result.data, safe=False)


@csrf_exempt
def campTagResult(request):
    if request.method == 'POST':
        try:
            taglist = json.loads(request.body)
            result = []
            for tagid in taglist:
                queryset = Campsite.objects.filter(campsite_id__in=Subquery(CampsiteTag.objects.filter(tag_id=tagid)
                                                                          .values('campsite_id'))).order_by('likeCount')[:50]
                serializer = CampsiteSerializer(queryset, many=True)
                result.append(serializer.data)

        except Campsite.DoesNotExist:
            return HttpResponse(status=404)

    return JsonResponse(result, safe=False)


def addlike(request):
    if request.method == 'GET':
        try:
            user_id=request.get['user_id']
            camp_id=request.get['camp_id']

            result=[]

        except Campsite.DoesNotExist:
            return HttpResponse(status=404)

    return JsonResponse("", safe=False)

@csrf_exempt
@api_view(['post'])
@permission_classes((permissions.AllowAny,))
def campCreateReview(request):
    if request.method == 'POST':
        print(request.data)
        serializer = CampCreateReviewSerializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse(status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            serializer.save()
            return JsonResponse("리뷰 등록 완료", safe=False, status=status.HTTP_201_CREATED)

def campReadReview(request, campsite_id):
    try:
        query_sets = Reviews.objects.filter(campsite_id = campsite_id)
    except Campsite.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET' and len(query_sets) > 0:
        serializer = CampReadReviewSerializer(query_sets, many=True)
        return JsonResponse(serializer.data, safe=False) 

    else:
        return JsonResponse("리뷰가 없습니다", safe=False) 

def campDeleteReview(request, review_id):
    review = Reviews.objects.get(review_id=review_id)
    review.delete()
    return JsonResponse("삭제 성공", safe=False, status=status.HTTP_201_CREATED)
