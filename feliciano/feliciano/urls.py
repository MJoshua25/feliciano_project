from django.contrib import admin
<<<<<<< HEAD
from django.urls import path ,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('resto.urls')),
    path('blog',include('blog_App.urls')),
    path('contacts',include('contacts.urls')),
    
=======
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from filebrowser.sites import site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainConfig.urls')),
    path('blog', include('blog_App.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('admin/filebrowser/', site.urls),
>>>>>>> 1a6b06a7928634800a8cb0b6516a150df176f43a
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)