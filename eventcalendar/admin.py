from django.contrib import admin

# Register your models here.
from eventcalendar import models 

# admin.site.register(Profile)
# admin.site.register(Skill)
# admin.site.register(Message)

@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    model = models.Event
    list_display = [
        "id",
        "title",
        "country",
        "user",
        "is_active",
        "is_deleted",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active", "is_deleted"]
    search_fields = ["title", "country"]


@admin.register(models.EventMember)
class EventMemberAdmin(admin.ModelAdmin):
    model = models.EventMember
    list_display = ["id", "event", "user", "created_at", "updated_at"]
    list_filter = ["event"]