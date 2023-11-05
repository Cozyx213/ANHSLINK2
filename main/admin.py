from django.contrib import admin
from .models import Post
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'author')
    date_hierarchy = 'created_at'

# Register your models here.
