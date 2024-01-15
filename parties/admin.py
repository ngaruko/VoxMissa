from django.contrib import admin

# Register your models here.
from .models import Tag, Party, Vote, Candidate, Policy, Message

admin.site.register(Party)
admin.site.register(Vote)
admin.site.register(Candidate)
admin.site.register(Policy)
admin.site.register(Message)
admin.site.register(Tag)