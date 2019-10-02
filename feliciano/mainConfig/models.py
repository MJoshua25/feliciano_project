from django.db import models

# Create your models here.
class config (models.Model):
    numero = models.CharField(max_length =225)
    adress = models.EmailField(max_length=225)
    logo = models.ImageField(blank=True, upload_to='img')
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)

class Slide (models.Model):
    nom = models.CharField(max_length =225)
    titre = models.CharField(max_length =225)
    image = models.ImageField(blank=True, upload_to='img')
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)
    
class Etape (models.Model):
    nom = models.CharField(max_length =225)
    image = models.ImageField(blank=True, upload_to='img')
    titre = models.CharField(max_length =225)
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)
    
class Footer (models.Model):
    titre = models.CharField(max_length =225)
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)

class foot_detail (models.Model):
    categorie = models.ForeignKey('Footer', on_delete = models.CASCADE, related_name = 'footer_detail')
    description = models.CharField(max_length =225, blank=True)
    jour = models.DateTimeField(auto_now_add= False, blank=True)
    heure_debut = models.TimeField(auto_now_add= False, blank=True)
    heure_fin = models.TimeField(auto_now_add= False, blank=True)
    image = models.ImageField(blank=True, upload_to='img')
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)
    

    
    