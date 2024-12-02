from django.urls import path
from . import views 

app_name = 'userapp'

urlpatterns = [
    path('login-signup/', views.login_signup, name='login_signup'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('profile/<str:username>/edit/', views.edit_profile, name='edit_profile'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('user/post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('logout/confirm/', views.logout_confirm, name='logout_confirm'),
]