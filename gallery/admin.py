from django.contrib import admin
from django.utils.html import format_html
from .models import Gallery, Image
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ['image_preview']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px; border-radius: 5px;">', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Preview'

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at', 'cover_preview', 'image_count']
    list_filter = ['created_at', 'user']
    search_fields = ['title', 'description']
    inlines = [ImageInline]
    
    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" style="max-height: 50px; border-radius: 5px;">', obj.cover_image.url)
        return "No Cover"
    cover_preview.short_description = 'Cover'
    
    def image_count(self, obj):
        count = obj.images.count()
        return format_html('<span class="badge" style="background-color: #17a2b8; color: white; padding: 5px 10px; border-radius: 10px;">{}</span>', count)
    image_count.short_description = 'Images'

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'gallery', 'image', 'caption']
    list_filter = ['gallery']
    search_fields = ['caption', 'gallery__title']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px; border-radius: 5px;">', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Preview'

