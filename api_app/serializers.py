from rest_framework import serializers
from .models import Event_Info


class Event_infoSerializer(serializers.ModelSerializer):
 class Meta:
  model = Event_Info
  fields = ['id', 'name', 'type', 'tagline', 'schedule', 'description', 'moderator', 'files', 'category', 'sub_category', 'rigor_rank', 'attendees']

    
