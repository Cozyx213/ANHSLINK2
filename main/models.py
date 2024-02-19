from django.db import models
from django.contrib.auth.models import User
import uuid, os
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.utils.text import slugify
from django.utils.timezone import timezone
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField (max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__ (self):
        return self.title + "\n" + self.description
    
    
def upload_to_function(instance, filename):
    return f'media/{instance.grade}/{instance.subject}/{filename}'


class Resources (models.Model):
    name = models.CharField(max_length=100, default='Default Name')
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    subject = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    file = models.FileField(upload_to= upload_to_function)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.grade +''+ self.subject
    
class Forum (models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default="")
    description = models.CharField(max_length=400, default="")
    
    uploaded_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, default="", related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    
    text = models.CharField(max_length=200)
    
    uploaded_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    
# Create your models here.
