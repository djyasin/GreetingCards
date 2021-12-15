from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django_toggle_m2m.toggle import ToggleManyToMany


# Create your models here.
#user model
class CustomUser(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


#tag model
class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag


#card model many to many? 
class Card(models.Model):
    title = models.CharField(max_length=250)
    message = models.TextField(max_length=500)
    custom_message = models.TextField(max_length=500)
    sender = models.CharField(max_length=250)
    recipient = models.CharField(max_length=250)
    favorited_by = models.ManyToManyField(
        CustomUser, related_name="favorite_cards", blank=True)
    date_created = models.DateTimeField(default=timezone.now, null=True)
    author = models.CharField(max_length=250)
    #image = models.image(freakin huge)
    public = models.BooleanField(default=True)
    tags = models.ManyToManyField(to=Tag, related_name="cards", blank=True)




