from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'TTT'

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('places/category/<int:category_id>/', views.places_by_category, name='places_by_category'),
]
