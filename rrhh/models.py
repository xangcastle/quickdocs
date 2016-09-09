from django.db import models


class Person(models.Model):
    MONEDAS = (
    ('CORDOBAS', 'CORDOBAS'),
    ('DOLARES', 'DOLARES'),
    )
    cedula = models.CharField(max_length=14)
    nombre = models.CharField(max_length=125, verbose_name="nombre completo")
    moneda = models.CharField(max_length=20, choices=MONEDAS, default="DOLARES")
    salario = models.FloatField(null=True)
    tc = models.FloatField(null=True, default=1.0, verbose_name="tasa de cambio")
    cuenta = models.CharField(max_length=25, null=True, verbose_name="cuenta a aplicar",
    help_text="cuenta banpro")
    fecha_ingreso = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.nombre

    def ir(self, monto):
        return round(monto * 0.1, 2)

    def inss(self, monto):
        return round(monto * 0.0625, 2)

    def patronal(self, monto):
        return round(monto * 0.185, 2)

    def inatec(self, monto):
        return round(monto * 0.02, 2)

    def pago_dias(self, dias):
        tarifa = round(self.salario / 30, 2)
        importe = round(tarifa * dias, 2)
        inss = self.inss(importe)
        ir = self.ir(importe - inss)
        inatec = self.inatec(importe)
        return {'id': self.id, 'cedula': self.cedula, 'nombre': self.nombre,
        'salario': self.salario, 'tarifa': tarifa, 'importe': importe,
        'inss': inss, 'patronal': self.patronal(importe), 'inatec': inatec,
        'ir': ir, 'monto': round(importe - (inss + ir), 2)}

    def pago_mes(self, quinsena, mes):
        if quinsena == "AMBAS":
            importe = self.salario
        else:
            importe = round(self.salario / 2, 2)
        inss = self.inss(importe)
        ir = self.ir(importe - inss)
        inatec = self.inatec(importe)
        return {'id': self.id, 'cedula': self.cedula, 'nombre': self.nombre,
        'salario': self.salario, 'importe': importe,
        'inss': inss, 'patronal': self.patronal(importe), 'inatec': inatec,
        'ir': ir, 'monto': round(importe - (inss + ir), 2)}


    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Servicios Profesionales"
