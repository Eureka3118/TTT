from django.urls import path
from . import views

urlpatterns = [
    path('', views.place_list, name='place_list'),
    path('category/<int:category_id>/', views.place_by_category, name='place_by_category'),
]
