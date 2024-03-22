from rest_framework import serializers
from .models import Forum, Post, Classroom, Comment
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
    like_count = serializers.IntegerField( read_only=True)
    comment_count = serializers.IntegerField( read_only=True)
    
    class Meta:
        model = Forum
        fields = ['id', 'title', 'description', 'author',"uploaded_at",'like_count','comment_count']
class CommentSerializer(serializers.ModelSerializer):
    
    author = AuthorSerializer(read_only=True)
    reply_count = serializers.IntegerField( read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'forum', 'text', 'author',"uploaded_at",'reply_count']
    
    
class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title','description', 'created_at','author','slug']
class ClassroomSerializer(serializers.ModelSerializer):
    teacher = AuthorSerializer(read_only=True)
    students = AuthorSerializer(read_only=True)
    class Meta:
        model =Classroom
        fields= ['id','name','teacher','students', 'student_count']