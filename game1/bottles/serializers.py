from rest_framework import serializers
from .models import Bottle, BottleItem
from userapp.models import Player
import random

class ShowBottleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BottleItem
        fields = ['name', 'points', 'distance']



class SendBottleSerializer(serializers.ModelSerializer):
    bottle_name = serializers.CharField(max_length=100)

    class Meta:
        model = Bottle
        fields = ['bottle_name', 'text']

class Read(serializers.ModelSerializer):
    class Meta:
        model = Bottle


class Response(serializers.ModelSerializer):
    class Meta:
        model = Player

class SendResponse(serializers.ModelSerializer):
    class Meta:
        model = Bottle
        fileds = ['response']