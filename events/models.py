from django.db import models

# Create your models here.

from email.policy import default
from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField

import time
from datetime import datetime

from users.models import Profile
# Create your models here.

class Event(models.Model):
    TYPES = (
       ('poll', 'poll'),
       ('meeting', 'meeting'),
       ('rally', 'rally'),
       ('election', 'election'),
       ('campaign', 'campaign'),
       ('other', 'other')
       
   )
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=50, choices=TYPES, default='poll')
    preview = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(Profile, blank=True, related_name='eventus')
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    registration_deadline = models.DateTimeField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-end_date']

    @property
    def event_status(self):
        status = None
        
        present = datetime.now().timestamp()
        deadline = self.registration_deadline.timestamp()
        past_deadline = (present > deadline)

        if past_deadline:
            status = 'Finished'
        else:
            status = 'Ongoing'

        return status


class Submission(models.Model):
    participant = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name="submissions")
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    details = models.TextField(null=True, blank=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.event) + ' --- ' + str(self.participant)
    
