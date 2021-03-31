from rest_framework import serializers
from .models import User


class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'nickname']


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','user_id','nickname']