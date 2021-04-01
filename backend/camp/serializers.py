from rest_framework import serializers
from .models import Campsite, Tag, Reviews


class CampsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campsite
        fields = ['campsite_id', 'campsite_name', 'doNm', 'sigunguNm', 'firstImageUrlV', 'likeCount']


class CampsiteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campsite
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['tag_id','tag_name']

class CampCreateReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = ['user_id','campsite_id','review']

class CampReadReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = ['user_id','campsite_id','review','review_id']

# class CampUpdateReviewSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = reviews
#         fields = ['user_id','campsite_id','review','review_id']
