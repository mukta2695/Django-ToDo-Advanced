from django.contrib import admin
from .models import Task
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shop

# Register your models here.

admin.site.register(Task)

@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')