from rest_framework import serializers
from .models import Campsite, Tag, Likes, Reviews, User, CampsiteTag


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
        fields = ['tag_id', 'tag_name']


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Likes
        fields = ['campsite_id', 'user_id']


class CampCreateReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = ['user_id','campsite_id','review','created_at']


class CampReadReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = ['user_id','campsite_id','review','review_id','created_at']


class CampReadReviewUSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['user_id','nickname']
