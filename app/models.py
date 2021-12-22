from django.utils import timezone
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django_toggle_m2m.toggle import ToggleManyToMany
from pygments import highlight 
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())



class CustomUser(AbstractUser):
    following = models.ManyToManyField("CustomUser", related_name='followers', blank=True)

    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username



class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag



class Card(models.Model):
    title = models.CharField(max_length=250)
    outer_message = models.TextField(max_length=500)
    inner_message = models.TextField(max_length=500)
    sender = models.CharField(max_length=250)
    recipient = models.CharField(max_length=250)
    favorited_by = models.ManyToManyField(
        CustomUser, related_name="favorite_cards", blank=True)
    date_created = models.DateTimeField(default=timezone.now, null=True)
    public = models.BooleanField(default=True)
    tags = models.ManyToManyField(to=Tag, related_name="cards", blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cards')
    outer_color = models.CharField(max_length=20, null=True)
    inner_color = models.CharField(max_length=20, null=True)
    outer_message_color = models.CharField(max_length=20, null=True)
    inner_message_color = models.CharField(max_length=20, null=True)
    inner_font = models.CharField(max_length=200, null=True)
    outer_font = models.CharField(max_length=200, null=True)
    outer_image = models.URLField(max_length=200, null=True)
    class Meta:
        ordering = ['-date_created']

        def __str__(self):
            return self.title
    

    
    

