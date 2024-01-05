from django.contrib import admin

# Register your models here.
from .models import Policy, Vote, Subtopic

admin.site.register(Policy)
admin.site.register(Vote)
admin.site.register(Subtopic)
