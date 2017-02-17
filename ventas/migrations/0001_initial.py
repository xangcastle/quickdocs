# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.FloatField(default=1.0, null=True)),
                ('codigo', models.CharField(max_length=25, null=True)),
                ('descripcion', models.CharField(max_length=125, null=True)),
                ('costo', models.FloatField(default=1.0, null=True)),
                ('precio', models.FloatField(default=1.0, null=True)),
                ('descuento', models.FloatField(default=1.0, null=True)),
                ('total', models.FloatField(default=1.0, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(max_length=8, null=True)),
                ('fecha', models.DateTimeField(null=True)),
                ('nombre', models.CharField(max_length=110, null=True)),
                ('identificacion', models.CharField(max_length=14, null=True, blank=True)),
                ('telefono', models.CharField(max_length=14, null=True, blank=True)),
                ('email', models.EmailField(max_length=120, null=True, blank=True)),
                ('direccion', models.TextField(max_length=14, null=True, blank=True)),
                ('subtotal', models.FloatField(default=b'0.0')),
                ('descuento', models.FloatField(default=b'0.0')),
                ('iva', models.FloatField(default=b'0.0')),
                ('total', models.FloatField(default=b'0.0')),
                ('costo', models.FloatField(default=b'0.0')),
                ('usuario', models.ForeignKey(related_name=b'ventas_factura_usuario', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='articulo',
            name='factura',
            field=models.ForeignKey(to='ventas.Factura'),
            preserve_default=True,
        ),
    ]
