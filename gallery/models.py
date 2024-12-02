from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from django.utils import timezone

class Gallery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='gallery_covers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery_images/')
    caption = models.CharField(max_length=255, blank=True)

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gallery_ratings')
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='ratings')
    value = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'gallery']
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} rated {self.gallery.title}: {self.value}"

class Picture(models.Model):
    image = models.ImageField(upload_to='gallery_pictures/')
    caption = models.CharField(max_length=255, blank=True)