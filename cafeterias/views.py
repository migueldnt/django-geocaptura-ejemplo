from django.shortcuts import render
from django.http import HttpResponse
from .models import Cafeteria
from django.core.serializers import serialize
import json
# Create your views here.
def mapa_v(request):
    cafeterias=Cafeteria.objects.all()
    geojson=serialize("geojson",cafeterias,geometry_field="ubicacion")
    return render(request,"cafeterias/mapa.html",{"cafeterias":geojson})

def geojson_v(request):
    cafeterias=Cafeteria.objects.all()
    geojson=serialize("geojson",cafeterias,geometry_field="ubicacion")
    response=HttpResponse(geojson,content_type="application/json")
    response["Access-Control-Allow-Origin"]="*"
    return response