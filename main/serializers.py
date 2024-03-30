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
    forum = ForumSerializer(read_only=True)
    author = AuthorSerializer(read_only=True)
    reply_count = serializers.IntegerField( read_only=True)
    parent = serializers.SerializerMethodField()
    def get_parent(self, obj):
        """
        This method is called for each Comment instance. If the comment has a parent,
        it will serialize the parent with the same serializer. If the comment doesn't
        have a parent, it will return None.
        """
        if obj.parent:
            # Serialize the parent with the same serializer
            return CommentSerializer(obj.parent, context=self.context).data
        else:
            # Return None if there is no parent
            return None
    class Meta:
        model = Comment
        fields = ['id', 'forum', 'text', 'author',"uploaded_at",'reply_count','parent']
    
    
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