from django.contrib import admin

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


class ItemsCommendeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'menu_id',
        'quantite',
        'prix_total',
        'date_add',
        'date_up',
        'status',
    )
    list_filter = (
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
_register(models.Article, ArticleAdmin)
_register(models.ItemsCommende, ItemsCommendeAdmin)
_register(models.Commende, CommendeAdmin)
_register(models.Service, ServiceAdmin)
_register(models.Info, InfoAdmin)
_register(models.Pub, PubAdmin)
_register(models.Reservation, ReservationAdmin)
