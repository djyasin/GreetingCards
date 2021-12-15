from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, User
from .models import Tag, Card, CustomUser

admin.site.register(Card)
admin.site.register(Tag)
admin.site.register(CustomUser, UserAdmin)