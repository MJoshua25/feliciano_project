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


class FrontAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'textLogo',
        'fixImage',
        'felicianoSlogan',
        'suscriberText',
        'performText',
        'dateAdd',
        'dateUpp',
        'status',
    )
    list_filter = (
        'dateAdd',
        'dateUpp',
        'status',
        'id',
        'textLogo',
        'fixImage',
        'felicianoSlogan',
        'suscriberText',
        'performText',
        'dateAdd',
        'dateUpp',
        'status',
    )


class headBackImageAdmin(admin.ModelAdmin):

    list_display = ('id', 'Image', 'text', 'status')
    list_filter = ('status', 'id', 'Image', 'text', 'status')


class AboutAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'aboutText',
        'aboutImages1',
        'aboutImages2',
        'status',
    )
    list_filter = (
        'status',
        'id',
        'aboutText',
        'aboutImages1',
        'aboutImages2',
        'status',
    )


class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'iconText',
        'serviceTtitle',
        'serviveDescription',
        'status',
    )
    list_filter = (
        'status',
        'id',
        'iconText',
        'serviceTtitle',
        'serviveDescription',
        'status',
    )


class contactAdmin(admin.ModelAdmin):

    list_display = ('id', 'phone', 'email', 'adresse')
    list_filter = ('id', 'phone', 'email', 'adresse')


class LocationMapAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'location_name',
        'long',
        'lal',
        'dateAdd',
        'dateUpp',
        'status',
    )
    list_filter = (
        'dateAdd',
        'dateUpp',
        'status',
        'id',
        'location_name',
        'long',
        'lal',
        'dateAdd',
        'dateUpp',
        'status',
    )


class settingAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'experiance',
        'number_menu',
        'staf_number',
        'cunstomer_number',
        'date_add',
        'date_upp',
        'status',
    )
    list_filter = (
        'date_add',
        'date_upp',
        'status',
        'id',
        'experiance',
        'number_menu',
        'staf_number',
        'cunstomer_number',
        'date_add',
        'date_upp',
        'status',
    )


class WorkingHoursAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'day',
        'openHours',
        'date_add',
        'date_upp',
        'status',
    )
    list_filter = (
        'day',
        'date_add',
        'date_upp',
        'status',
        'id',
        'day',
        'openHours',
        'date_add',
        'date_upp',
        'status',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.config, configAdmin)
_register(models.Front, FrontAdmin)
_register(models.headBackImage, headBackImageAdmin)
_register(models.About, AboutAdmin)
_register(models.Service, ServiceAdmin)
_register(models.contact, contactAdmin)
_register(models.LocationMap, LocationMapAdmin)
_register(models.setting, settingAdmin)
_register(models.WorkingHours, WorkingHoursAdmin)
