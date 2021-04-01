from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Subquery
import json
from django.db.models import Q
from .models import Campsite, CampsiteTag, Tag
from .serializers import CampsiteSerializer, CampsiteDetailSerializer, TagSerializer
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
            query = CampsiteTag.objects.filter(campsite_id__in=Subquery(
                Campsite.objects.filter(Q(campsite_name__icontains=searchword)| Q(addr1__icontains=searchword)|
                                        Q(indutyV__icontains=searchword)).values('campsite_id')
            )).values('campsite_id', 'tag_id').order_by('tag_id')

            result = []
            idx = -1
            default = 0

            for id in query:
                campid = id.get('campsite_id')
                tagid = id.get('tag_id')

                qs = Campsite.objects.filter(pk=campid)
                tg = Tag.objects.filter(pk=tagid)

                camp = CampsiteSerializer(qs, many=True)
                tag = TagSerializer(tg, many=True)

                if default != tagid:
                    line = []
                    idx = idx+1
                    line.append(tag.data)
                    line.append(camp.data)
                    result.append(line)
                    default = tagid
                else:
                    result[idx].append(camp.data)

        except Campsite.DoesNotExist:
            return HttpResponse(status=404)

    return JsonResponse(result, safe=False)


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


        except Campsite.DoesNotExist:
            return HttpResponse(status=404)

    return JsonResponse(result, safe=False)
