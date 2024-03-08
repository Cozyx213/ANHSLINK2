from rest_framework import serializers
from .models import Forum, Post
from authentication.models import Profile
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
class AuthorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ['user','section','email','grade']

class ForumSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Forum
        fields = ['id', 'title', 'description', 'author',"uploaded_at"]

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title','description', 'created_at','author']