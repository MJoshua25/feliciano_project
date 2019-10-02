from django.contrib import admin
from django.utils.safestring import mark_safe
# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CategorieAdmin(admin.ModelAdmin):

    list_display = ('id', 'titre', 'date_add', 'date_up', 'status')
    list_filter = (
        'date_add',
        'date_up',
        'status',
        'id',
        'titre',
        'date_add',
        'date_up',
        'status',
    )


<<<<<<< HEAD
class MenuAdmin(admin.ModelAdmin):

    list_display = (
        'afficheMenu',
        'id',
        'cat_id',
        'titre',
        'description',
        'image_menu',
        'prix',
        'date_add',
        'date_up',
        'status',
    )
    list_filter = (
        'cat_id',
        'date_add',
        'date_up',
        'status',
        'id',
        'cat_id',
        'titre',
        'description',
        'prix',
        'date_add',
        'date_up',
        'status',
    )
    
   
    def afficheMenu(self,obj):
        return mark_safe('<img src="{url}" width=50 height=50></img>'.format(url=obj.image_menu.url))

=======
class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'auteur',
        'categorie',
        'titre',
        'description',
        'image',
        'prix',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'auteur',
        'categorie',
        'statut',
        'date_add',
        'date_update',
        'id',
        'auteur',
        'categorie',
        'titre',
        'description',
        'image',
        'prix',
        'statut',
        'date_add',
        'date_update',
    )
>>>>>>> 1a6b06a7928634800a8cb0b6516a150df176f43a


class ItemsCommendeAdmin(admin.ModelAdmin):

    list_display = (
<<<<<<< HEAD
        'afficheMenu',
=======
>>>>>>> 1a6b06a7928634800a8cb0b6516a150df176f43a
        'id',
        'menu_id',
        'quantite',
        'prix_total',
        'date_add',
        'date_up',
        'status',
    )
    list_filter = (
<<<<<<< HEAD
        
=======
>>>>>>> 1a6b06a7928634800a8cb0b6516a150df176f43a
        'menu_id',
        'date_add',
        'date_up',
        'status',
        'id',
        'menu_id',
        'quantite',
        'prix_total',
        'date_add',
        'date_up',
        'status',
    )

<<<<<<< HEAD
    def afficheMenu(self,obj):
        return mark_safe('<img src="{url}" width=50 height=50></img>'.format(url=obj.menu_id.image_menu.url))
=======
>>>>>>> 1a6b06a7928634800a8cb0b6516a150df176f43a

class CommendeAdmin(admin.ModelAdmin):

    list_display = ('id', 'client_id', 'date_add', 'date_up', 'status')
    list_filter = (
        'client_id',
        'date_add',
        'date_up',
        'status',
        'id',
        'client_id',
        'date_add',
        'date_up',
        'status',
    )
    raw_id_fields = ('Items_id',)


<<<<<<< HEAD
=======
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'icon',
        'titre',
        'description',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'icon',
        'titre',
        'description',
        'statut',
        'date_add',
        'date_update',
    )


class InfoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nombre',
        'titre',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'nombre',
        'titre',
        'statut',
        'date_add',
        'date_update',
    )


class PubAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'icon',
        'titre',
        'description',
        'image1',
        'image2',
        'jour_debut',
        'jour_fin',
        'heure_debut',
        'heure_fin',
        'contact',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'jour_debut',
        'jour_fin',
        'statut',
        'date_add',
        'date_update',
        'id',
        'icon',
        'titre',
        'description',
        'image1',
        'image2',
        'jour_debut',
        'jour_fin',
        'heure_debut',
        'heure_fin',
        'contact',
        'statut',
        'date_add',
        'date_update',
    )


>>>>>>> 1a6b06a7928634800a8cb0b6516a150df176f43a
class ReservationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'email',
        'phone',
        'date',
        'time',
        'place_number',
        'date_add',
        'date_up',
        'status',
    )
    list_filter = (
        'date',
        'date_add',
        'date_up',
        'status',
        'id',
        'name',
        'email',
        'phone',
        'date',
        'time',
        'place_number',
        'date_add',
        'date_up',
        'status',
    )
    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Categorie, CategorieAdmin)
<<<<<<< HEAD
_register(models.Menu, MenuAdmin)
_register(models.ItemsCommende, ItemsCommendeAdmin)
_register(models.Commende, CommendeAdmin)
=======
_register(models.Article, ArticleAdmin)
_register(models.ItemsCommende, ItemsCommendeAdmin)
_register(models.Commende, CommendeAdmin)
_register(models.Service, ServiceAdmin)
_register(models.Info, InfoAdmin)
_register(models.Pub, PubAdmin)
>>>>>>> 1a6b06a7928634800a8cb0b6516a150df176f43a
_register(models.Reservation, ReservationAdmin)
