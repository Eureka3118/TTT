from django.contrib import admin
from .models import Category, Place

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'place_count', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'

    def place_count(self, obj):
        return obj.places.count()
    place_count.short_description = 'Number of Places'

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'location', 'rating', 'is_active', 'created_at')
    list_filter = ('category', 'is_active', 'created_at', 'rating')
    search_fields = ('name', 'description', 'location', 'category__name')
    autocomplete_fields = ['category']
    date_hierarchy = 'created_at'
    list_per_page = 20
    list_editable = ('is_active', 'category')
    actions = ['activate_places', 'deactivate_places']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'description')
        }),
        ('Location Details', {
            'fields': ('location', 'latitude', 'longitude')
        }),
        ('Media', {
            'fields': ('image',),
            'classes': ('collapse',)
        }),
        ('Status', {
            'fields': ('is_active', 'rating')
        }),
    )

    def activate_places(self, request, queryset):
        queryset.update(is_active=True)
    activate_places.short_description = "Mark selected places as active"

    def deactivate_places(self, request, queryset):
        queryset.update(is_active=False)
    deactivate_places.short_description = "Mark selected places as inactive"

    def get_ordering(self, request):
        return ['-created_at']  # Default ordering by creation date
