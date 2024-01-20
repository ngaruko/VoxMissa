from django.test import TestCase

# Create your tests here.
from datetime import datetime
from django.db import models
from django.urls import reverse
from django_countries import countries, Countries
from core.utils import Africa

from users.models import Profile


class EventAbstract(models.Model):
    """ Event abstract model """

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class EventManager(models.Manager):
    """ Event manager """

    def get_all_events(self, user):
        events = Event.objects.filter(user=user, is_active=True, is_deleted=False)
        return events

    def get_running_events(self, user):
        running_events = Event.objects.filter(
            user=user,
            is_active=True,
            is_deleted=False,
            end_time__gte=datetime.now().date(),
        ).order_by("start_time")
        return running_events

class G8Countries(Countries):
    only = [
        "CA", "FR", "DE", "IT", "JP", "RU", "GB"
    ]
class Event(EventAbstract):
    TYPES = (
       ('poll', 'poll'),
       ('meeting', 'meeting'),
       ('rally', 'rally'),
       ('election', 'election'),
       ('campaign', 'campaign'),
       ('other', 'other')
       
   )
    """ Event model """

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="events")
    country = models.CharField(max_length=200, blank=True, null=True, choices=Africa)
    type = models.CharField(max_length=50, choices=TYPES, default='election')
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    objects = EventManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("event-detail", args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse("event-detail", args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'


class EventMember(EventAbstract):
    """ Event member model """

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="events")
    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="event_members"
    )

    class Meta:
        unique_together = ["event", "user"]

    def __str__(self):
        return str(self.user)
