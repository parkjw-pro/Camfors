from rest_framework import serializers
from .models import Campsite


class CampsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Campsite
        fields=['campsite_name', 'lineintro', 'addr1']



