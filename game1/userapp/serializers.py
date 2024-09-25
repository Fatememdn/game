from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Player
import random

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['user','x', 'y']

    def create(self, validated_data):
        user_data  = validated_data.pop('user') 
        user = User.objects.create_user(**user_data)
        validated_data['x'] = random.randint(0, 100)
        validated_data['y'] = random.randint(0, 100)
        player = Player.objects.create(user=user, **validated_data)
        return player


        







