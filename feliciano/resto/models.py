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
    
<<<<<<< HEAD
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
=======
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
>>>>>>> 1a6b06a7928634800a8cb0b6516a150df176f43a

class ItemsCommende(models.Model):
    menu_id=models.ForeignKey(Article,on_delete=models.CASCADE,related_name='Article_items')
    quantite=models.IntegerField()
<<<<<<< HEAD
    prix_total=models.DecimalField(max_length=255,max_digits=10,decimal_places=5)
=======
    prix_total=models.DecimalField(max_digits=20, decimal_places=4)
>>>>>>> 1a6b06a7928634800a8cb0b6516a150df176f43a
    date_add=models.DateTimeField(auto_now_add=True)
    date_up=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)

    
class Commende(models.Model):
    client_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='User_commende')
    Items_id=models.ManyToManyField(ItemsCommende,related_name='Item_commende')
    date_add=models.DateTimeField(auto_now_add=True)
    date_up=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)
        
<<<<<<< HEAD
    def __str__(self):
        return self.client_id
            
=======
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
>>>>>>> 1a6b06a7928634800a8cb0b6516a150df176f43a
    
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
    def __str__(self):
        return self.name
