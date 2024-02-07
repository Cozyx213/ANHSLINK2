from django.contrib import admin
from .models import Post
from django.contrib import admin
from .models import Post, Resources

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'author')
    date_hierarchy = 'created_at'

@admin.register(Resources)
class ResourcesAdmin(admin.ModelAdmin):
    list_display = ('file', 'author', 'uploaded_at')
    search_fields = ('subject', 'grade')
    list_filter = ('uploaded_at', 'author')
    date_hierarchy = 'uploaded_at'
# Register your models here.
