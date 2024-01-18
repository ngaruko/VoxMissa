from django.contrib import admin

# Register your models here.

from .models import Event, Submission

admin.site.register(Event)
admin.site.register(Submission)