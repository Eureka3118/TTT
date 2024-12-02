from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', include('TTT.urls')),  
    path('user/', include('userapp.urls')),
    path('blog/', include('blog.urls')),
    path('gallery/', include('gallery.urls')),
    path('destinations/', include('destinations.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
