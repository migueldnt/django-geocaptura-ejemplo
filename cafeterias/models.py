#from django.db import models
from django.contrib.gis.db import models

# Create your models here.


class Cafeteria(models.Model):
    nombre=models.CharField(max_length=100)
    cantidad_personal=models.IntegerField()
    calidad_servicio=models.CharField(max_length=10,choices=[("m","Malo"),("b","Bueno"),("e","Excelente")])
    ubicacion=models.PointField()

    def __str__(self):
        return self.nombre
