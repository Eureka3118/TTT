from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
from .models import Gallery, Image

class GalleryStats:
    def __init__(self):
        self.title = 'Gallery Statistics'
    
    def get_data(self):
        end_date = timezone.now()
        start_date = end_date - timedelta(days=30)
        
        gallery_data = (
            Gallery.objects.filter(
                created_at__range=(start_date, end_date)
            ).extra(
                select={'date': 'date(created_at)'}
            ).values('date').annotate(
                count=Count('id')
            ).order_by('date')
        )
        
        labels = [str(item['date']) for item in gallery_data]
        data = [item['count'] for item in gallery_data]
        
        return {
            'labels': labels,
            'datasets': [{
                'label': 'Galleries Created',
                'data': data,
                'backgroundColor': 'rgba(54, 162, 235, 0.2)',
                'borderColor': 'rgba(54, 162, 235, 1)',
                'borderWidth': 1
            }]
        }

class ImageStats:
    def __init__(self):
        self.title = 'Image Distribution'
    
    def get_data(self):
        image_data = (
            Image.objects.values(
                'gallery__title'
            ).annotate(
                count=Count('id')
            ).order_by('-count')[:5]
        )
        
        labels = [item['gallery__title'] or 'Untitled' for item in image_data]
        data = [item['count'] for item in image_data]
        
        return {
            'labels': labels,
            'datasets': [{
                'label': 'Images per Gallery',
                'data': data,
                'backgroundColor': [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                ],
                'borderColor': [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                ],
                'borderWidth': 1
            }]
        } 