from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Resources, Forum, Comment
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]
        
class ResourceForm (forms.ModelForm):
    
    class Meta:
        model = Resources
        fields = ["grade", "subject", "file","description"]
class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ["title", "description"]
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields= ["text"]