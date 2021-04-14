from django.db import models
from django.utils import timezone

class Song(models.Model):
    ID=models.IntegerField(unique=True,primary_key=True)
    name=models.CharField(max_length=100)
    duration=models.PositiveIntegerField()
    uploaded_time=models.DateTimeField(auto_now=True)

class Podcast(models.Model):
    ID=models.IntegerField(unique=True,primary_key=True)
    name=models.CharField(max_length=100)
    duration=models.PositiveIntegerField()
    uploaded_time=models.DateTimeField(auto_now=True)
    host=models.CharField(max_length=100)
    participants=models.TextField()
    
class AudioBook(models.Model):
    ID=models.IntegerField(unique=True,primary_key=True)
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    narrator=models.CharField(max_length=100)
    duration=models.PositiveIntegerField()
    uploaded_time=models.DateTimeField(auto_now=True)
