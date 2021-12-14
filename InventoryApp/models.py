from os import truncate
from django.db import models
from datetime import datetime, timedelta
# Create your models here.

class Inventory(models.Model) :
    codigo = models.CharField(max_length = 30)
    marca = models.CharField(max_length = 30)
    descripcion = models.CharField(max_length = 100)
    ubicacion = models.CharField(max_length = 30)
    unidad = models.CharField(max_length = 30)
    stock = models.IntegerField()
    dolares = models.DecimalField(max_digits = 8, decimal_places = 2)
    soles = models.DecimalField(max_digits = 10, decimal_places = 2)
    valor_del_stock = models.DecimalField(max_digits = 9, decimal_places = 2)
    tipo_de_cambio = models.DecimalField(max_digits = 5, decimal_places = 2)
    def __str__(self):
        return (self.descripcion)