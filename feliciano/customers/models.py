from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
# Appel de user
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')  # 1 user <---> 1 profil
    # Champs suplementaires
    image = models.ImageField(upload_to='Customer/', default='useravatar.png')
    # Initialisation a la creation
    @receiver(post_save, sender=User)
    def create_user_customer(sender, instance, created, **kwargs):
        if created:
            Customer.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_customer(sender, instance, created, **kwargs):
                
        instance.customer.save()
        

class MasterChef(models.Model):
    nom = models.CharField(max_length=255)
    fontion=models.CharField(max_length=255)
    image = models.ImageField(upload_to='MasterChef/', default='useravatar.png')
    fb_link=models.URLField()
    tw_link=models.URLField()
    g_link=models.URLField()
    insta_link=models.URLField()
    
        

class Testi(models.Model):
    customer_id=models.ForeignKey(Customer ,on_delete=models.CASCADE, related_name='customer')
    comment=models.TextField()
    date_add=models.DateTimeField(auto_now_add=True)
    date_up=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)
    