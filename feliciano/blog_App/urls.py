from django.contrib import admin
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('',views.blog ,name='blog'),
    path('single_blog',views.single_blog ,name='single_blog'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
