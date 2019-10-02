from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class configAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'numero',
        'adress',
        'logo',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'numero',
        'adress',
        'logo',
        'statut',
        'date_add',
        'date_update',
    )


class SlideAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'titre',
        'image',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'nom',
        'titre',
        'image',
        'statut',
        'date_add',
        'date_update',
    )


class EtapeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'image',
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
        'nom',
        'image',
        'titre',
        'statut',
        'date_add',
        'date_update',
    )


class FooterAdmin(admin.ModelAdmin):

    list_display = ('id', 'titre', 'statut', 'date_add', 'date_update')
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'titre',
        'statut',
        'date_add',
        'date_update',
    )


class foot_detailAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'categorie',
        'description',
        'jour',
        'heure_debut',
        'heure_fin',
        'image',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'categorie',
        'jour',
        'statut',
        'date_add',
        'date_update',
        'id',
        'categorie',
        'description',
        'jour',
        'heure_debut',
        'heure_fin',
        'image',
        'statut',
        'date_add',
        'date_update',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.config, configAdmin)
_register(models.Slide, SlideAdmin)
_register(models.Etape, EtapeAdmin)
_register(models.Footer, FooterAdmin)
_register(models.foot_detail, foot_detailAdmin)
