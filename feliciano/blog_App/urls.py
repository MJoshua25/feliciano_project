from django.urls import path
from .import views

app_name='blog'

urlpatterns = [
    path('',views.index ,name='index'),
    path('article/<int:id>',views.article ,name='article'),
    path('category/<str:cat>',views.category ,name='category'),
    path('tag/<str:tag>',views.category ,name='tag'),
    path('date/<int:annee>/<int:mois>',views.category ,name='date'),
    path('fake',views.artFake),
]
