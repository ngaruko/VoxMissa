from django.db import models
from django_resized import ResizedImageField

# Create your models here.
from django.db import models
import uuid
from django_countries.fields import CountryField
from django.db.models.deletion import CASCADE
from core.settings import MEDIA_ROOT
from core.utils import Africa
from forum.models import Topic
from users.models import Profile
from policies.models import Topic, Subtopic
# Create your models here.


class Party(models.Model):
    country = CountryField(null=True, choices=Africa)
    #country = models.CharField(max_length=200, choices=Africa)
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    acronym = models.CharField(max_length=100, null=True, blank=True)
    leader = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    policies = models.ManyToManyField('Policy', null=True)
    official_logo = ResizedImageField(size=[100, 100], 
        null=True, blank=True, default= "party_logo.jpeg")
    website = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True, null=True)
    ideology =  models.CharField(max_length=200, null=True, blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-vote_ratio', '-vote_total', 'name']
        verbose_name_plural = "parties"

    @property
    def imageURL(self):
        try:
            url = self.official_logo.url
        except:
            print('No image URL found')
            url = ''
        return url
    


    @property
    def reviewers(self):
        queryset = self.vote_set.all().values_list('voter__id', flat=True)
        return queryset

    @property
    def getVoteCount(self):
        reviews = self.vote_set.all()
        upVotes = reviews.filter(value='up').count()
        totalVotes = reviews.count()

        ratio = (upVotes / totalVotes) * 100
        self.vote_total = totalVotes
        self.vote_ratio = ratio

        self.save()


class Vote(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    voter = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='party_voter')
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    class Meta:
        unique_together = [['voter', 'party']]
        

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)


    def __str__(self):
        return self.name

class Candidate(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE,  null=True)
    featured_image = models.ImageField(
        null=True, blank=True, default="default.jpg")
    name = models.CharField(max_length=200)
    bio = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name
    
class Policy(models.Model):
    owner = models.ForeignKey(
        Party, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(
        null=True, blank=True, default="default.jpg")
    topic = models.ForeignKey(
        Topic, null=True, blank=True, on_delete=models.SET_NULL)
    subtopic = models.ForeignKey(
        Subtopic, null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-vote_ratio', '-vote_total', 'title']
        verbose_name_plural = "policies"

    @property
    def imageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url

    @property
    def reviewers(self):
        queryset = self.vote_set.all().values_list('owner__id', flat=True)
        return queryset

    @property
    def getVoteCount(self):
        reviews = self.vote_set.all()
        upVotes = reviews.filter(value='up').count()
        totalVotes = reviews.count()

        ratio = (upVotes / totalVotes) * 100
        self.vote_total = totalVotes
        self.vote_ratio = ratio

        self.save()


class Message(models.Model):
    sender = models.ForeignKey(
        Party, on_delete=models.SET_NULL, null=True, blank=True, related_name='representative')
    recipient = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="citizen")
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', '-created']

    