from django.db import models


class Person(models.Model):
    cedula = models.CharField(max_length=14)
    nombre = models.CharField(max_length=125, verbose_name="nombre completo")
    hora = models.FloatField(verbose_name="precio/hora")
    
    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Servicios Profecionales"
