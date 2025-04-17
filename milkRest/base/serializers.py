from .models import *
from rest_framework import serializers



class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        exclude = ['id']