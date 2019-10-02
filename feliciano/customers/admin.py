# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CustomerAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'image')
    list_filter = ('user', 'id', 'user', 'image')


class MasterChefAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'fontion',
        'image',
        'fb_link',
        'tw_link',
        'g_link',
        'insta_link',
    )
    list_filter = (
        'id',
        'nom',
        'fontion',
        'image',
        'fb_link',
        'tw_link',
        'g_link',
        'insta_link',
    )


class TestiAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'customer_id',
        'comment',
        'date_add',
        'date_up',
        'status',
    )
    list_filter = (
        'customer_id',
        'date_add',
        'date_up',
        'status',
        'id',
        'customer_id',
        'comment',
        'date_add',
        'date_up',
        'status',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Customer, CustomerAdmin)
_register(models.MasterChef, MasterChefAdmin)
_register(models.Testi, TestiAdmin)
