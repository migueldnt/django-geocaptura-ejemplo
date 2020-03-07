from django.urls import path,include
from .views import mapa_v,geojson_v

urlpatterns=[
    path("mapa",mapa_v),
    path("geojson",geojson_v)
]