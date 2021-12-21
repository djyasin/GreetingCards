from django.shortcuts import render
from rest_framework import generics
from .models import Card, Tag, CustomUser 
from .serializers import CardSerializer, CustomUserCreateSerializer, CustomUserSerializer, TagSerializer
from rest_framework.generics import RetrieveAPIView,  CreateAPIView, ListCreateAPIView, ListAPIView, RetrieveDestroyAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer



class UserCreatedList(generics.ListCreateAPIView):
        serializer_class = CardSerializer

        def get_queryset(self):
            user = self.request.user
            return Card.objects.filter(author=user)


class AddCard(CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class EditCard(RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class DeleteCard(RetrieveDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class NewCard(CreateAPIView):
    serializer_class = CardSerializer

class NewUser(CreateAPIView):
    serializer_class = CustomUserCreateSerializer

class UserList(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserDetail(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class FollowView(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class FavoritedView(RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer