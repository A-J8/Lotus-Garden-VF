from distutils.command.upload import upload
from django.db import models

from LotusGarden.settings import MEDIA_URL

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    imagen =models.ImageField(upload_to='media/')
    descripcion = models.CharField(max_length=500, default='')
    estado_promocion = models.BooleanField(default=False)
    precio_antiguo = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.nombre}'

class Promocion(models.Model):
    fecha_inicio = models.DateField(blank=True, null=True)   
    fecha_termino = models.DateField(blank=True, null=True)   
    descuento = models.IntegerField(null= True, default=0)
    id_producto = models.IntegerField(default=0)

class Historial(models.Model):
    fecha = models.DateField(null=False, default='2020-07-08')
    total = models.IntegerField(default=0)

class Suscripcion(models.Model):
    nombre = models.CharField(null=False, max_length=30)
    fecha_suscripcion = models.DateField(null=False)
    descuento = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)

    