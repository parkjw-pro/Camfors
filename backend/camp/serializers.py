from rest_framework import serializers
<<<<<<< HEAD
from .models import Campsite, Tag, Likes
=======
from .models import Campsite, Tag, Reviews
>>>>>>> da34a12757ade6f75ab8fb289765badb0bc9fa91


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
        fields = ['user_id','campsite_id','review']

class CampReadReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = ['user_id','campsite_id','review','review_id']
