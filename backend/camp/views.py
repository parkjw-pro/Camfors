from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Subquery
import json
from django.db.models import Q

from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework import status
from .models import Campsite, CampsiteTag, Tag, Reviews, Likes, User
from .serializers import CampsiteSerializer, CampsiteDetailSerializer, CampCreateReviewSerializer, CampReadReviewSerializer, TagSerializer, CampReadReviewUSerializer, LikeSerializer
from django.db.models import Count
import collections

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# jsonparser로 requset body 데이터 얻을수 있음


# 서비스 단위 하나
def campsitelist(request):
    if request.method == 'GET':
        query_sets = Campsite.objects.all()
        serializer = CampsiteSerializer(query_sets, many=True)
        return JsonResponse(serializer.data, safe=False)


def campsitedetail(request, pk):
    try:
        campsite = Campsite.objects.get(pk=pk)
    except Campsite.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CampsiteDetailSerializer(campsite)

        # 태그 추가
        sub_result = collections.OrderedDict()
        camp_id = serializer.data['campsite_id']
        # sub_queryset = Tag.objects.filter(campsite_id=camp_id).values('tag_id')
        sub_queryset = Tag.objects.raw(
            '''select tag_id
            from Campsite_Tag
            where campsite_id = {campsite_id}'''.format(campsite_id=camp_id)
        )
        sub_serializer = TagSerializer(sub_queryset, many = True)
        for k, v in serializer.data.items():
            sub_result[k] = v
        sub_result['taglist'] = sub_serializer.data
        # print(sub_result)

        return JsonResponse(sub_result, safe=False)


def camptaglist(request, tag_id):
    try:
        query_sets = Campsite.objects.filter(campsite_id__in=Subquery(CampsiteTag.objects
                                                                      .filter(tag_id=tag_id)
                                                                      .values('campsite_id')))[:20]
    except Campsite.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET' and len(query_sets) > 0:
        serializer = CampsiteSerializer(query_sets, many=True)

        return JsonResponse(serializer.data, safe=False)

    else:
        return JsonResponse("조회된 데이터가 없습니다.", safe=False)


def camplikeslist(request):
    try:
        query_sets = Campsite.objects.all().order_by('-likeCount')[:20]
    except Campsite.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET' and len(query_sets) > 0:
        serializer = CampsiteSerializer(query_sets, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def campwordresult(request):
    if request.method == 'POST':
        try:
            word = json.loads(request.body)
            searchword = word.get('word')
            query = Campsite.objects.filter(Q(campsite_name__icontains=searchword) | Q(addr1__icontains=searchword) |
                                            Q(glampInnerFclty__icontains=searchword) |
                                            Q(posblFcltyCl__icontains=searchword) | Q(exprnProgrm__icontains=searchword) |
                                            Q(themaEnvrnCl__icontains=searchword) | Q(eqpmnLendCl__icontains=searchword)).distinct()
            serializer = CampsiteSerializer(query, many=True)

        except Campsite.DoesNotExist:
            return HttpResponse(status=404)

    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def camptagresult(request):
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


def gettaglist(request):
    if request.method == 'GET':
        try:
            query = Tag.objects.all()
            taglist = TagSerializer(query, many=True)

        except Tag.DoesNotExist:
            return HttpResponse(status=404)

    return JsonResponse(taglist.data, safe=False)


def listbyuser(request, user_id):
    if request.method == 'GET':
        try:
            check = Likes.objects.filter(user_id=user_id).aggregate(Count('campsite_id'))
            cnt = check.get('campsite_id__count')
            if cnt > 0:
                query = Tag.objects.raw('''SELECT tag_id, count(campsite_id) FROM CFS.Campsite_Tag 
                    where campsite_id in (select campsite_id from Likes where user_id={user_id}) 
                    group by tag_id order by count(campsite_id) desc
                    limit 5;'''.format(user_id=user_id))
                serializer = TagSerializer(query, many=True)

            else:
                query = Tag.objects.raw(
                    '''select ct.tag_id , sum(c.likeCount) as tagLikeCount 
                        from Campsite c, Campsite_Tag ct  
                        where c.campsite_id = ct.campsite_id 
                        GROUP BY ct.tag_id
                        order by tagLikeCount desc
                        limit 5'''
                )
                serializer = TagSerializer(query, many=True)

        except Campsite.DoesNotExist:
            return HttpResponse(status=404)

    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def camppoptagresult(request):
    try:
        query_sets = Tag.objects.raw(
            '''select ct.tag_id , sum(c.likeCount) as tagLikeCount 
                from Campsite c, Campsite_Tag ct  
                where c.campsite_id = ct.campsite_id 
                GROUP BY ct.tag_id
                order by tagLikeCount desc
                limit 5'''
        )

    except Tag.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET' and len(query_sets) > 0:
        serializer = TagSerializer(query_sets, many=True)
        return JsonResponse(serializer.data, safe=False) 


@csrf_exempt
def addlike(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body).get('data')

            serializer = LikeSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                camp = Campsite.objects.get(pk=data.get('campsite_id'))
                camp.likeCount = camp.likeCount+1
                camp.save()
            else:
                print("invalid")

        except Campsite.DoesNotExist:
            return HttpResponse(status=404)

    return JsonResponse("true", safe=False)


@csrf_exempt
def unlike(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body).get('data')

            object = Likes.objects.filter(campsite_id=data.get('campsite_id'), user_id=data.get('user_id'))
            object.delete()

            camp = Campsite.objects.get(pk=data.get('campsite_id'))
            camp.likeCount = camp.likeCount-1
            camp.save()

        except Campsite.DoesNotExist:
            return HttpResponse(status=404)

    return JsonResponse("false", safe=False)


def getlikeinfo(request):
    if request.method == 'GET':
        try:
            userid = request.GET.get('userId', None)
            campid = request.GET.get('campsiteId', None)

            query = Likes.objects.filter(user_id=userid, campsite_id=campid).aggregate(Count('campsite_id'))

        except Campsite.DoesNotExist:
            return HttpResponse(status=404)

    return HttpResponse(query.get('campsite_id__count'))


@csrf_exempt
def camprecommend(request,campsite_id):
    data = pd.read_csv("data.csv",encoding = 'euc-kr')

    count_vector = CountVectorizer(ngram_range=(1,1))
    c_vector_tag = count_vector.fit_transform(data['태그'])

    tag_c_sim = cosine_similarity(c_vector_tag,c_vector_tag).argsort()[:,::-1]

    # 코사인 유사도를 이용하여 단어의 유사도를 통해 추천
    def get_recommend_camping_list(data,camping_index,top=30):
        target_camping_index = data[data['캠핑장ID'] == camping_index].index.values
    
        sim_index = tag_c_sim[target_camping_index, :top].reshape(-1)
    
        sim_index = sim_index[sim_index != target_camping_index]
        result = data.iloc[sim_index][:10]
        return result

    result = []
    recom = get_recommend_camping_list(data,camping_index = campsite_id)
    for i in recom['캠핑장ID']:
        query_sets = Campsite.objects.filter(campsite_id = i)
        serializer = CampsiteSerializer(query_sets, many=True)
        result.append(serializer.data)

    return JsonResponse(result, safe=False, status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['post'])
@permission_classes((permissions.AllowAny,))
def campcreatereview(request):
    if request.method == 'POST':
        print(request.data)
        serializer = CampCreateReviewSerializer(data=request.data)
        print(serializer)
        if not serializer.is_valid():
            return JsonResponse(status= status.HTTP_406_NOT_ACCEPTABLE)
        else:
            serializer.save()
            return JsonResponse("리뷰 등록 완료", safe=False, status=status.HTTP_201_CREATED)


@csrf_exempt
def campreadreview(request, campsite_id):
    try:
        query_sets = Reviews.objects.raw(
            '''select R.campsite_id, R.created_at, R.review, U.nickname, R.review_id 
            from User as U, Reviews as R 
            where U.user_id = R.user_id
            and R.campsite_id = {campsite_id}
            order by created_at desc'''.format(campsite_id=campsite_id)
        )

    except Reviews.DoesNotExist:
        return HttpResponse(status=404)

    try:
        query_sets2 = User.objects.raw(
            '''select U.user_id, R.campsite_id, R.created_at, R.review, U.nickname, R.review_id 
            from User as U, Reviews as R 
            where U.user_id = R.user_id
            and R.campsite_id = {campsite_id}
            order by created_at desc'''.format(campsite_id = campsite_id)
        )

    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET' and len(query_sets) > 0 and len(query_sets2) > 0:
        serializer = CampReadReviewSerializer(query_sets, many=True)
        serializer2 = CampReadReviewUSerializer(query_sets2, many=True)
        result = []
        review_len = len(serializer.data)
        for i in range(review_len):
            sub_result = collections.OrderedDict()
            for k, v in serializer.data[i].items():
                sub_result[k] = v
            for k, v in serializer2.data[i].items():
                sub_result[k] = v
            result.append(sub_result)
        return JsonResponse(result, safe=False) 

    else:
        return JsonResponse("리뷰가 없습니다", safe=False) 


@csrf_exempt
def campdeletereview(request, review_id):
    review = Reviews.objects.filter(review_id=review_id)
    review.delete()
    return JsonResponse("삭제 성공", safe=False, status=status.HTTP_201_CREATED)
