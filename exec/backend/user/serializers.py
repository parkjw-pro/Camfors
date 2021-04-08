from rest_framework import serializers
from .models import User
from .models import Campsite
from .models import Likes
from .models import Reviews

class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'nickname']


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','user_id','nickname']

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['campsite_id','user_id','review','created_at','review_id']

class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campsite
        fields = ['campsite_id','campsite_name','doNm','sigunguNm','firstImageUrlV','likeCount']
