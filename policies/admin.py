from django.contrib import admin

# Register your models here.
from .models import Topic, Subtopic

admin.site.register(Topic)
admin.site.register(Subtopic)
