from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField
# Create your models here.
from decimal import Decimal

class Categorie(models.Model):
    titre=models.CharField(max_length=255)
    date_add=models.DateTimeField(auto_now_add=True)
    date_up=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)
    
class Article (models.Model):
    auteur =  models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user_article',)
    categorie = models.ForeignKey('Categorie', on_delete = models.CASCADE, related_name = 'categorie_article')
    titre = models.CharField(max_length =225)
    description = models.CharField(max_length =225)
    image = models.ImageField(blank=True, upload_to='img')
    prix = models.IntegerField()
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)

class ItemsCommende(models.Model):
    menu_id=models.ForeignKey(Article,on_delete=models.CASCADE,related_name='Article_items')
    quantite=models.IntegerField()
    prix_total=models.DecimalField(max_digits=20, decimal_places=4)
    date_add=models.DateTimeField(auto_now_add=True)
    date_up=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)

    
class Commende(models.Model):
    client_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='User_commende')
    Items_id=models.ManyToManyField(ItemsCommende,related_name='Item_commende')
    date_add=models.DateTimeField(auto_now_add=True)
    date_up=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)
        
class Service (models.Model):
    icon = models.CharField(max_length =225)
    titre = models.CharField(max_length =225)
    description = models.CharField(max_length =225)
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)

class Info (models.Model):
    nombre = models.IntegerField()
    titre = models.CharField(max_length =225)
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)

class Pub (models.Model):
    icon = models.CharField(max_length =225)
    titre = models.CharField(max_length =225)
    description = models.CharField(max_length =225)
    image1 = models.ImageField(blank=True, upload_to='img')
    image2 = models.ImageField(blank=True, upload_to='img')
    jour_debut = models.DateTimeField(auto_now_add= False)
    jour_fin = models.DateTimeField(auto_now_add= False)
    heure_debut = models.TimeField(auto_now_add= False)
    heure_fin = models.TimeField(auto_now_add= False)
    contact = models.TimeField(auto_now_add= False)
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)
    
class Reservation(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=255)
    date=models.DateField()
    time=models.TimeField()
    place_number=models.IntegerField()
    date_add=models.DateTimeField(auto_now_add=True)
    date_up=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)