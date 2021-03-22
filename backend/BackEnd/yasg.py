from django.conf.urls import url
from django.urls import path, include
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny,IsAuthenticated,BasePermission
from drf_yasg import openapi

schema_url_patterns = [
    path('main/', include('main.urls')),
]
schema_view = get_schema_view(
    openapi.Info(
        title="캠퍼스(Camping For Smart)",
        default_version='v1',
        description=
        '''
        # 캠핑장 정보 및 리뷰를 통한 사용자 기반 캠핑장 추천 홈페이지
        
        ---
        ## 맴버
        ### 팀장 
        이태환
        ### 프론트
        신다정
        박종원
        이태환
        ### 백앤드
        송기헌
        김낙영
        ''',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="xoghks11397@naver.com"),
        license = openapi.License(name = "이태환"),
    ),
    validators=['flex'],
    public=True,
    permission_classes=(AllowAny,),
    patterns=schema_url_patterns,
)
