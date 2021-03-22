from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import CampsiteSerializer
from .models import Campsite

@api_view(['GET'])
def camp_list(request):
    '''
    하나의 캠핑장 정보를 조회하는 api

    ---
    ## `/main`
    ## 내용
        -
    '''

    camp = Campsite.objects.all()
    serializers = CampsiteSerializer(camp, many=True)
    return Response(serializers.data[0])