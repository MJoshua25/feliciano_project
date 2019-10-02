from django.db import models

# Create your models here.

class Front(models.Model):
    textLogo=models.CharField(max_length=255)
    fixImage=models.ImageField(upload_to='Front/fixe_images')
    felicianoSlogan=models.TextField()
    suscriberText=models.CharField(max_length=255)
    performText=models.CharField(max_length=255)
    dateAdd=models.DateTimeField(auto_now_add=True)
    dateUpp=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)
    
class headBackImage(models.Model):
    Image=models.ImageField(upload_to='Front/backHeadImages')
    text=models.CharField(max_length=255,null=True)
    status=models.BooleanField(default=True)
    
class About(models.Model):
    aboutText=models.TextField()
    aboutImages1 =models.ImageField(upload_to='About')
    aboutImages2 =models.ImageField(upload_to='About')
    status=models.BooleanField(default=True)

class Service(models.Model):
    iconText=models.CharField(max_length=255)
    serviceTtitle=models.CharField(max_length=255)
    serviveDescription=models.TextField()
    status=models.BooleanField(default=True)
    
class WorkingHours(models.Model):
    day=models.DateField()
    openHoures=models.TimeField()
    closeHoures=models.TimeField()
    dateAdd=models.DateTimeField(auto_now_add=True)
    dateUpp=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)
    

class contact(models.Model):
    phone=models.CharField(max_length=255)
    email=models.EmailField()
    adresse=models.CharField(max_length=255)
    
class LocationMap(models.Model):
    location_name=models.CharField(max_length=255)
    long=models.DecimalField(max_length=255,max_digits=10,decimal_places=5)
    lal=models.DecimalField(max_length=255,max_digits=10,decimal_places=5)
    dateAdd=models.DateTimeField(auto_now_add=True)
    dateUpp=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)
        
        
class setting(models.Model):
    experiance=models.IntegerField()
    number_menu=models.IntegerField()
    staf_number=models.IntegerField()
    cunstomer_number=models.IntegerField()
    date_add=models.DateTimeField(auto_now_add=True)
    date_upp=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)
    