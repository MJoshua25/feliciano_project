# MODEL Josué

## Contact_app
```python
class Message(models.Model):
# TODO: Define fields here
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    sujet = models.CharField(max_length=50)
    message = models.TextField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
    	return '{}'.format(self.sujet)

class Newsletter(models.Model):
    # TODO: Define fields here
    email = models.EmailField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Newsletter"
        verbose_name_plural = "Newsletters"

    def __str__(self):
        return self.email
```

## Blog_app
```python
from restaurant_app.models import Category

class Article(models.Model):
    titre = models.CharField(max_length=250)
    description = models.TextField()
    contenu = HTMLField('contenu')
    image = models.ImageField(upload_to='blog/articles')
    category = models.ForeignKey('Category',on_delete=models.CASCADE,related_name='category_arcticle')
    author = models.ForeignKey('Author',on_delete=models.CASCADE,related_name='author_article')
    tag = models.ManyToManyField('Tag')
    acceuil = models.BooleanField(default=True,null=True)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return '{} {}'.format(self.titre,self.author)



class Tag(models.Model):
    # TODO: Define fields here
    titre = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return '{}'.format(self.titre)

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='article_comment')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='auteur', null=True)
    image = models.ImageField(upload_to='blog/comment',default='profile/default.png, null=True)
    message = models.TextField()
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=255, null=True)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return '{}'.format(self.name)


class Author(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='auteur')
    image = models.ImageField(upload_to='blog/author')
    description = models.TextField()
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return '{}'.format(self.user)
```
## mainConfig_app patrick
```python
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
    dateAdd=models.DateTimeField(auto_now_add=True)
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

```
    
## customers_app patrick
```python
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
    
```






# feliciano_project
 Projet feliciano
 
 ## Aplications.
 >Apres analyse,pour mieux structure notre projet je trouve qu'il serra utilis de le subdivisee en quatres (4) appications
 ### MainConfig
 >   Cette applications serrs dedier aux parametrage generale du site ,tout ce qui est front ,visible sur le site et qui ne necessite 
 >   aucune interactions .
 >   L'applications contients les informations du site comme les contacts les heurs d'ouvertures la localisations et autres 
 ### Customers
 >   Cette applications serra dedier a la gestions aux utilisateurs de notre site (client , visiteur et personnel ).
 ### Restorants 
 >   Pour la gestions des commendes ,l'ajout et la mise a jours des differents menu .
 ### Blog
 >   comme vous l'avez dejat constate 
 >   Mais je pense qu'il y des trucs a revoir au niveau de certaines tables 
 
 ## Models

###================= Application Blog ===============#

```python

from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField

#================= Application Blog ===============#

class Categorie (models.Model):
    nom = models.CharField(max_length =225)
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.nom

class Article (models.Model):
    auteur =  models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'categorie_user',)
    categorie = models.ForeignKey('Categorie', on_delete = models.CASCADE, related_name = 'categorie_article')
    tag = models.ManyToManyField(Tag)
    titre = models.CharField(max_length =225)
    description = models.HTMLField('description')
    contenue = models.HTMLField('contenue')
    image = models.ImageField(blank=True, upload_to='img')
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add= True)
    date_update = models.DateTimeField(auto_now= True)

class Commentaire (models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'Commentair_user',)
    article = models.ForeignKey(Article, on_delete = models.CASCADE, related_name = 'article_commente',)
    contenue = models.CharField(max_length=225)
    date_add = models.DateTimeField ( auto_now_add = True )
    date_upd = models.DateTimeField ( auto_now = True )
    statut = models.BooleanField ( default = True )

class Reponse_Commentaire (models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'Repose_user',)
    commentaire = models.ForeignKey(Commentaire, on_delete = models.CASCADE, related_name = 'commente_rep',)
    contenue = models.CharField(max_length=225)
    date_add = models.DateTimeField ( auto_now_add = True )
    date_upd = models.DateTimeField ( auto_now = True )
    statut = models.BooleanField ( default = True )

class Reponse_RepCommentaire (models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'Repose_user',)
    commentaire = models.ForeignKey(Reponse_Commentaire, on_delete = models.CASCADE, related_name = 'commente_rep_rep',)
    contenue = models.CharField(max_length=225)
    date_add = models.DateTimeField ( auto_now_add = True )
    date_upd = models.DateTimeField ( auto_now = True )
    statut = models.BooleanField ( default = True )

class Tag (models.Model):
    nom = models.CharField ( max_length = 255 )


```
