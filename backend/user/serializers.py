from rest_framework import serializers
from .models import User
from .models import Campsite
from .models import Likes
from .models import reviews

class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'nickname']


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','user_id','nickname']

class reviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = reviews
        fields = ['campsite_id','user_id','review']

class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campsite
        fields = ['campsite_id','campsite_name','doNm','sigunguNm','firstImageUrlV','likeCount']
