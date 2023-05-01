from django.db import models

# Create your models here.

class Event_Info(models.Model):
   
    type=models.CharField(max_length=100) 
    name=models.CharField(max_length=100) 
    tagline=models.CharField(max_length=100)
    schedule=models.DateTimeField()
    description=models.CharField(max_length=300)
    files=models.FileField(blank=True, null=True)
    moderator=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    sub_category=models.CharField(max_length=100)
    rigor_rank=models.IntegerField()
    attendees=models.CharField(max_length=100)

