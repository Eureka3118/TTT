# blog/admin.py

from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'content', 'author__username')
    date_hierarchy = 'created_at'
    list_per_page = 20
    actions = ['publish_posts', 'unpublish_posts']
    

    def is_published(self, obj):
        return True if obj.created_at else False
    is_published.boolean = True
    is_published.short_description = 'Published'

    def publish_posts(self, request, queryset):
        queryset.update(is_published=True)
    publish_posts.short_description = "Mark selected posts as published"

    def unpublish_posts(self, request, queryset):
        queryset.update(is_published=False)
    unpublish_posts.short_description = "Mark selected posts as unpublished"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('short_content', 'author', 'post', 'created_at')
    list_filter = ('author', 'created_at', 'post')
    search_fields = ('content', 'author__username', 'post__title')
    date_hierarchy = 'created_at'
    list_per_page = 50

    def short_content(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    short_content.short_description = 'Comment'
