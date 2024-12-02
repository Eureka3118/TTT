from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('search/', views.search_posts, name='search_posts'),
    path('create/', views.post_create, name='post_create'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('blog/post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('post/<int:post_id>/delete/', views.post_delete, name='post_delete'),
]
