
from django.contrib import admin
from .models import Post, Resources, Forum, Comment, Classroom, Grade, Section, Subject
from django.urls import reverse
from django.utils.html import format_html
from django import forms
from django.contrib import admin


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display=["level","id"]
    
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display= ["name","grade","id"]
    list_filter=["grade"]
    
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display=["name","grade","id"]
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ('title', 'author', 'created_at', 'updated_at','slug')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'author')
    date_hierarchy = 'created_at'

@admin.register(Resources)
class ResourcesAdmin(admin.ModelAdmin):
    
    list_display = ('file', 'name', 'author', 'uploaded_at','uuid',"is_approved","download_link","description")
    search_fields = ('subject', 'grade')
    list_filter = ('uploaded_at', 'author','grade','subject')
    date_hierarchy = 'uploaded_at'
    actions = ["approve_posts"]
    
    def approve_posts(self, request, queryset):
        queryset.update(is_approved=True)
    def download_link(self, obj):
        return format_html(f'<a href = "{reverse("download", args=[obj.uuid])}" >Download </a>')
    approve_posts.short_description = "Mark selected posts is approved"
    
@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ("title","author", "uploaded_at","like_count")
    actions = ["approve_posts"]
    
@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("text","author","parent", "forum", "uploaded_at")
    list_filter = ("parent","forum","uploaded_at")
    
@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display= ("teacher",  "name")
# Register your models here.
 