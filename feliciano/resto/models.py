from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categorie(models.Model):
    titre=models.CharField(max_length=255)
    date_add=models.DateTimeField(auto_now_add=True)
    date_up=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)
    
class Menu(models.Model):
    cat_id=models.ForeignKey(Categorie,on_delete=models.CASCADE,related_name='Categorie_menu')
    titre=models.CharField(max_length=255)
    description=models.TextField()
    prix=models.DecimalField(max_length=255)
    date_add=models.DateTimeField(auto_now_add=True)
    date_up=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)

class ItemsCommende(models.Model):
    menu_id=models.ForeignKey(Menu,on_delete=models.CASCADE,related_name='Menu_items')
    quantite=models.IntegerField()
    prix_total=models.DecimalField(max_length=255)
    date_add=models.DateTimeField(auto_now_add=True)
    date_up=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)

    
class Commende(models.Model):
    client_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='User_commende')
    Items_id=models.ManyToManyField(ItemsCommende,related_name='Item_commende')
    date_add=models.DateTimeField(auto_now_add=True)
    date_up=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)
        
    
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