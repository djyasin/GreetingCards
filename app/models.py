from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django_toggle_m2m.toggle import ToggleManyToMany
from pygments import highlight 
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


# Create your models here.
# user model profile image?
class CustomUser(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


# tag model
class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag


# card model many to many? 
class Card(models.Model):
    title = models.CharField(max_length=250)
    outer_message = models.TextField(max_length=500)
    inner_message = models.TextField(max_length=500)
    sender = models.CharField(max_length=250)
    recipient = models.CharField(max_length=250)
    favorited_by = models.ManyToManyField(
        CustomUser, related_name="favorite_cards", blank=True)
    date_created = models.DateTimeField(default=timezone.now, null=True)
    author = models.CharField(max_length=250)
    #image = models.image(freakin huge)
    public = models.BooleanField(default=True)
    tags = models.ManyToManyField(to=Tag, related_name="cards", blank=True)
    
    class Meta:
        ordering = ['-date_created']

    def save(self, *args, **kwargs):
        
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Card, self).save(*args, **kwargs)
        def __str__(self):
            return self.title
    # outer color
    # inner color
    # outer message color (font color)
    # inner message color (font color)
    # outer font 
    # inner font



