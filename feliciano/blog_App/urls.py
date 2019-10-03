from django.urls import path
from .import views

app_name='blog'

urlpatterns = [
    path('',views.index ,name='index'),
    path('article/<int:id>',views.article ,name='article'),
    path('category/<str:cat>',views.category ,name='category'),
    path('tag/<str:tag>',views.tag ,name='tag'),
    path('search',views.search,name='search'),
    path('date/<int:annee>/<int:mois>',views.category ,name='date'),
    path('commentaire',views.commentaire ,name='commentaire'),
    path('fake',views.artFake),
    path('fakecom',views.comFake),
]
