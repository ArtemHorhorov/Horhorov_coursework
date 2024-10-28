from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    users = models.ManyToManyField(User, related_name='events')

class Location(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='locations')
    tags = models.ManyToManyField('Tag', related_name='locations', blank=True)

class Tag(models.Model):
    name = models.CharField(max_length=30)
 

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)

class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class Comment(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(default='')


 

