from django.db import models

# Create your models here.

class Front(models.Model):
    textLogo=models.CharField(max_length=255)
    sliderText1=models.CharField(max_length=255)
    sliderText2=models.CharField(max_length=255)
    sliderText3=models.CharField(max_length=255)
    fixImage=models.ImageField(upload_to='Front/fixe_images')
    felicianoSlogan=models.TextField()
    suscriberText=models.CharField(max_length=255)
    performText=models.CharField(max_length=255)
    dateAdd=models.DateTimeField(auto_now_add==True)
    dateUpp=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)
    
class About(models.Model):
    aboutText=models.TextField()
    aboutImages1 =models.ImageField(upload_to='About')
    aboutImages2 =models.ImageField(upload_to='About')

class Service(models.Model):
    iconText=models.CharField(max_length=255)
    serviceTtitle=models.CharField(max_length=255)
    serviveDescription=models.TextField()
    
class WorkingHours(models.Model):
    day=models.DateField()
    openHoures=models.TimeField()
    closeHoures=models.TimeField()
    dateAdd=models.DateTimeField(auto_now_add=True)
    dateUpp=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)
    

    
    