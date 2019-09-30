# feliciano_project
 Projet feliciano
 
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
