# posts/serializers.py
from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        
        fields = ('id','name','address','phone_number',)
        model= models.post