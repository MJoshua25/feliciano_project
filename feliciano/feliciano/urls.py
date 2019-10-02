from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('resto.urls')),
    path('blog',include('blog_App.urls')),
    path('contacts',include('contacts.urls')),
    
]
