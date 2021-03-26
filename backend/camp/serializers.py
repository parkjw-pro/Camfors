from rest_framework import serializers
from .models import Campsite


class CampsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campsite
        fields = ['campsite_id','campsite_name', 'doNm', 'sigunguNm', 'firstImageUrlV', 'likeCount']


class CampsiteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campsite
        fields = '__all__'


