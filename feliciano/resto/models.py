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
    
    def __str__(self):
        return self.titre
    
class Menu(models.Model):
    cat_id=models.ForeignKey(Categorie,on_delete=models.CASCADE,related_name='Categorie_menu')
    titre=models.CharField(max_length=255)
    description=models.TextField()
    prix=models.DecimalField(max_length=255,max_digits=10,decimal_places=5)
    image_menu=models.ImageField(upload_to='Menu')
    date_add=models.DateTimeField(auto_now_add=True)
    date_up=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)
    def __str__(self):
        return self.titre

class ItemsCommende(models.Model):
    menu_id=models.ForeignKey(Menu,on_delete=models.CASCADE,related_name='Menu_items')
    quantite=models.IntegerField()
    prix_total=models.DecimalField(max_length=255,max_digits=10,decimal_places=5)
    date_add=models.DateTimeField(auto_now_add=True)
    date_up=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)

    
class Commende(models.Model):
    client_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='User_commende')
    Items_id=models.ManyToManyField(ItemsCommende,related_name='Item_commende')
    date_add=models.DateTimeField(auto_now_add=True)
    date_up=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)
        
    def __str__(self):
        return self.client_id
            


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
    date=models.CharField(max_length=255)
    time=models.CharField(max_length=255)
    place_number=models.CharField(max_length=255)
    date_add=models.DateTimeField(auto_now_add=True)
    date_up=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)
    def __str__(self):
        return self.name
