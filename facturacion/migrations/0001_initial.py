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
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name='codigo', blank=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name='nombre')),
                ('identificacion', models.CharField(help_text='RUC/CEDULA', max_length=14, null=True, blank=True)),
                ('telefono', models.CharField(max_length=25, null=True, blank=True)),
                ('email', models.EmailField(max_length=165, null=True, blank=True)),
                ('direccion', models.TextField(max_length=400, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name='codigo', blank=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name='nombre')),
                ('cantidad', models.FloatField(null=True)),
                ('precio', models.FloatField(null=True)),
                ('descuento', models.FloatField(null=True)),
                ('iva', models.FloatField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name='codigo', blank=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name='nombre')),
                ('identificacion', models.CharField(help_text='RUC/CEDULA', max_length=14, null=True, blank=True)),
                ('telefono', models.CharField(max_length=25, null=True, blank=True)),
                ('email', models.EmailField(max_length=165, null=True, blank=True)),
                ('direccion', models.TextField(max_length=400, null=True, blank=True)),
                ('numero', models.CharField(max_length=25, null=True, blank=True)),
                ('fecha', models.DateTimeField(auto_now_add=True, null=True)),
                ('subtotal', models.FloatField(null=True, blank=True)),
                ('descuento', models.FloatField(null=True, blank=True)),
                ('iva', models.FloatField(null=True, blank=True)),
                ('ir', models.FloatField(null=True, blank=True)),
                ('al', models.FloatField(null=True, blank=True)),
                ('total', models.FloatField(null=True, blank=True)),
                ('aplica_iva', models.BooleanField(default=True)),
                ('aplica_ir', models.BooleanField(default=False)),
                ('aplica_al', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(to='facturacion.Cliente', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name='codigo', blank=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name='nombre')),
                ('precio', models.FloatField(null=True)),
                ('costo', models.FloatField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='detalle',
            name='factura',
            field=models.ForeignKey(to='facturacion.Factura'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detalle',
            name='producto',
            field=models.ForeignKey(to='facturacion.Producto', null=True),
            preserve_default=True,
        ),
    ]
