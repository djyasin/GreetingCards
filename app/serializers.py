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
        'outer_color',
        'inner_color',
        'outer_message_color',
        'inner_message_color',
        'outer_font',
        'inner_font',
        'outer_image',
        )


class CustomUserCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ("username", "email", "password")


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "following")


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('tag')


