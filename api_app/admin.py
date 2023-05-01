from django.contrib import admin
from .models import Event_Info
# Register your models here.

@admin.register(Event_Info)

class Event_InfoAdmin(admin.ModelAdmin):
    list_display=['id', 'type','name', 'tagline', 'schedule', 'description', 'files', 'moderator', 'category', 'sub_category', 'rigor_rank', 'attendees']
    

