from django.contrib import admin

# Register your models here.
from .models import Party, Vote, Candidate

admin.site.register(Party)
admin.site.register(Vote)
admin.site.register(Candidate)
