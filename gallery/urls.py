from django.urls import path
from . import views
from .views import gallery_list, gallery_create

app_name = 'gallery'

urlpatterns = [
    path('', gallery_list, name='gallery_list'), 
    path('create/', gallery_create, name='gallery_create'),
    path('<int:pk>/', views.gallery_detail, name='gallery_detail'),
    path('<int:gallery_id>/upload/', views.upload_gallery_image, name='upload_gallery_image'),
    path('gallery/rate/<int:gallery_id>/', views.rate_gallery, name='rate_gallery'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('edit/<int:pk>/', views.gallery_edit, name='gallery_edit'),
]
