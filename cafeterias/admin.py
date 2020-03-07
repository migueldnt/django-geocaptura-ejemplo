#from django.contrib import admin
from django.contrib.gis import admin
from.models import Cafeteria
# Register your models here.

class MyCustomGeoAdmin(admin.OSMGeoAdmin):
    default_lon=-11350000
    default_lat=2519000
    default_zoom=5

admin.site.register(Cafeteria,MyCustomGeoAdmin)