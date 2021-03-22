from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import Campsite
from .serializers import CampsiteSerializer

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
        serializer = CampsiteSerializer(campsite)
        return JsonResponse(serializer.data, safe=False)

