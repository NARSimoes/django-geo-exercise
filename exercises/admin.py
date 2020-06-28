
from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from .models import Storage


@admin.register(Storage)
class StorageAdmin(OSMGeoAdmin):
    list_display = ('id', 'point')