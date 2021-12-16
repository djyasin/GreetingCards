from rest_framework import serializers
from .models import Card, Tag, CustomUser 


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ('title',
        'outer_message',
        'inner_message',
        'sender',
        'recipient',
        'favorited_by',
        'date_created',
        'author',
        'public',
        'tags',
        )


class CustomUserCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password")


class CustomUserSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField()

    class Meta:
        model = CustomUser
        fields = ("pk", "username", "photo")


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('tag')
