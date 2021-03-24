from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Subquery
from .models import Campsite, CampsiteTag
from .serializers import CampsiteSerializer,CampsiteDetailSerializer
# jsonparser로 requset body 데이터 얻을수 있음


# 서비스 단위 하나
@csrf_exempt
def campSite_list(request):
    if request.method == 'GET':
        query_sets = Campsite.objects.all()
        serializer = CampsiteSerializer(query_sets, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def campSite_detail(request, pk):
    try:
        campsite = Campsite.objects.get(pk=pk)
    except Campsite.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CampsiteDetailSerializer(campsite)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def camptaglist(request, tag_id):
    try:
        query_sets = Campsite.objects.filter(campsite_id__in=Subquery(CampsiteTag.objects
                                                                      .filter(tag_id=tag_id)
                                                                      .values('campsite_id'))).order_by("likeCount")[:20]
    except Campsite.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET' and len(query_sets) > 0:
        serializer = CampsiteSerializer(query_sets, many=True)
        return JsonResponse(serializer.data, safe=False)

    else:
        return JsonResponse("조회된 데이터가 없습니다.", safe=False)


@csrf_exempt
def campLikesList(request):
    try:
        campsite = Campsite.objects.get()
    except Campsite.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = campLikesListSerializer(campsite,many=True)
        return JsonResponse(serializer.data, safe=False)
