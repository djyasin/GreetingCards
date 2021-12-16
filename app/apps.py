from django.apps import AppConfig
from django.contrib import admin
from django.urls import include, path 


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'



