from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
# Appel de user
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')  # 1 user <---> 1 profil
    # Champs suplementaires
    image = models.ImageField(upload_to='profile/', default='useravatar.png')
    # Initialisation a la creation
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, created, **kwargs):
                
        instance.profile.save()
        

class MasterChef(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer') 
    image = models.ImageField(upload_to='profile/', default='useravatar.png')
    fb_link=models.URLField()
    tw_link=models.URLField()
    g_link=models.URLField()
    insta_link=models.URLField()
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            MasterChef.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, created, **kwargs):
                    
        instance.MasterChef.save()
        

class Testi(models.Model):
    customer_id=models.ForeignKey(Customer ,on_delete=models.CASCADE, related_name='customer')
    comment=models.TextField()
    date_add=models.DateTimeField(auto_now_add=True)
    date_up=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)
    