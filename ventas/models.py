from django.db import models
from django.contrib.auth.models import User


class Factura(models.Model):
    usuario = models.ForeignKey(User, null=True, related_name="ventas_factura_usuario")
    numero = models.CharField(max_length=8, null=True)
    fecha = models.DateTimeField(null=True)

    nombre = models.CharField(max_length=110, null=True)
    identificacion = models.CharField(max_length=14, null=True, blank=True)
    telefono = models.CharField(max_length=14, null=True, blank=True)
    email = models.EmailField(max_length=120, null=True, blank=True)
    direccion = models.TextField(max_length=400, null=True, blank=True)

    subtotal = models.FloatField(default="0.0")
    descuento = models.FloatField(default="0.0")
    iva = models.FloatField(default="0.0")
    total = models.FloatField(default="0.0")
    costo = models.FloatField(default="0.0")
    utilidad = models.FloatField(default="0.0")


class Articulo(models.Model):
    factura = models.ForeignKey(Factura)
    cantidad = models.FloatField(null=True, default=1.0)
    codigo = models.CharField(max_length=25, null=True)
    descripcion = models.CharField(max_length=125, null=True)
    costo = models.FloatField(null=True, default=0.0)
    precio = models.FloatField(null=True, default=0.0)
    descuento = models.FloatField(null=True, default=0.0)
    total = models.FloatField(null=True, default=0.0)
