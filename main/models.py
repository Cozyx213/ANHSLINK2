from django.db import models
from django.contrib.auth.models import User
import uuid, os
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.utils.text import slugify
from django.utils.timezone import timezone
from authentication.models import Profile
import random

def generate_unique_slug():
    
    return slugify(str(uuid.uuid4()))

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField (max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, default=uuid.uuid1)
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
        
    def __str__ (self):
        return self.title + "\n" + self.description
    
def upload_to_function(instance, filename):
    return f'media/{instance.grade}/{instance.subject}/{filename}'


class Grade(models.Model):
    level = models.IntegerField(default = 9)
    
    def __str__(self):
        return str(self.level)
class Section(models.Model):
    name = models.CharField(max_length=50, default="Apple")
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
class Subject(models.Model):
    name = models.CharField(max_length=50, default="A subject")
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
class Resources (models.Model):
    description = models.CharField(max_length=100, default='A file')
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    file = models.FileField(upload_to= upload_to_function)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='Default Name')
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.grade) +''+ str(self.subject)
    def name_file(self):
        return self.file
class Forum (models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="author")
    title = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=400, default="",blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name ='liked_comments')
    dislikes = models.ManyToManyField(User,related_name ='disliked_comments')
    def __str__(self):
        return self.title
    def comment_count(self):
        return self.comments.count()
    def comments_ordered(self):
        return self.comments.all().order_by('-uploaded_at')
    
    @property
    def like_count(self):
        return (self.likes.count() - self.dislikes.count())
    
class Comment(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, null=True, blank=True, default="", related_name='comments')
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null= True, blank=True, related_name ="replies")
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, default="")
    
    text = models.CharField(max_length=400)
    
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
 
    
    def __str__(self):
        return self.text
    def reply_count(self):
        return self.replies.count()
    def reply_ordered(self):
        return self.replies.all().order_by('-uploaded_at')
    
    
class Classroom(models.Model):
    name = models.CharField(max_length=12)
    teacher = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="teacher")
    students = models.ManyToManyField(Profile, related_name="students")
    
    
    @property
    def student_count(self):
        return self.students.count()
# Create your models here.
