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



class ItemsCommendeAdmin(admin.ModelAdmin):

    list_display = (
        'afficheMenu',
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

    def afficheMenu(self,obj):
        return mark_safe('<img src="{url}" width=50 height=50></img>'.format(url=obj.menu_id.image_menu.url))

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
_register(models.Menu, MenuAdmin)
_register(models.ItemsCommende, ItemsCommendeAdmin)
_register(models.Commende, CommendeAdmin)
_register(models.Reservation, ReservationAdmin)
