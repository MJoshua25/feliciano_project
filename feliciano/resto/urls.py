from django.contrib import admin
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('',views.index ,name='index'),
    path('about',views.about ,name='about'),
    path('menu',views.menu ,name='menu'),
    path('reservations',views.reservations ,name='reservations'),
    path('Souscriber',views.Souscriber,name='Souscriber'),
]