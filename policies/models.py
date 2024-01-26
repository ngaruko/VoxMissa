from django.db import models

# Create your models here.
from django.db import models
import uuid

from django.db.models.deletion import CASCADE
from core.utils import Africa
from users.models import Profile
# Create your models here.
from django_countries.fields import CountryField
from django.utils.text import slugify
from django.conf import settings

class Topic(models.Model):
    # country = models.CharField(max_length=200, blank=True, null=True, choices=Africa)
    # owner = models.ForeignKey(
    #     Profile, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    subtopics= models.ManyToManyField('Subtopic', verbose_name="list of subtopics", blank=True)
    featured_image = models.ImageField(
        null=True, blank=True, default="default.jpg")
    created = models.DateTimeField(auto_now_add=True, null=True)
    id = models.CharField(max_length=200, default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        

    @property
    def imageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name
      
class Subtopic(models.Model):
    policy = models.ForeignKey(Topic, on_delete=models.SET_NULL,  null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    id = models.CharField(max_length=200, default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name