# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import digitalizacion.models
from django.conf import settings
import multifilefield.models
import metropolitana.models


class Migration(migrations.Migration):

    dependencies = [
        ('metropolitana', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idempleado', models.PositiveIntegerField(null=True, verbose_name=b'codigo de empleado', blank=True)),
                ('nombre', models.CharField(max_length=120, null=True, blank=True)),
                ('cedula', models.CharField(max_length=14, null=True, blank=True)),
                ('gerencia', models.CharField(max_length=65, null=True, blank=True)),
                ('localidad', models.CharField(max_length=65, null=True, blank=True)),
                ('ecuenta', models.FileField(upload_to=metropolitana.models.get_media_url, null=True, verbose_name=b'estado de cuenta', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Impresion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_verificacion', models.DateTimeField(auto_now=True, verbose_name=b'fecha de carga')),
                ('consecutivo', models.PositiveIntegerField()),
                ('archivo', models.CharField(max_length=100, null=True, blank=True)),
                ('paquete', models.ForeignKey(to='metropolitana.Paquete')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['consecutivo'],
                'db_table': 'metropolitana_impresion',
                'verbose_name_plural': 'impresion de comprobantes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Indexacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('archivos', multifilefield.models.MultiFileField(null=True, upload_to=digitalizacion.models.get_path, blank=True)),
                ('carpeta', models.CharField(max_length=8, null=True)),
                ('make_ocr', models.BooleanField(default=False, verbose_name=b'hacer ocr')),
            ],
            options={
                'verbose_name': 'archivos pdf',
                'verbose_name_plural': 'carga de imagenes masiva',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('archivo', models.FileField(upload_to=b'TEMP')),
                ('archivos', multifilefield.models.MultiFileField(null=True, upload_to=b'', blank=True)),
                ('aplicar_ocr', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'archivos',
                'verbose_name_plural': 'carga de archivos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='import_paquete',
            fields=[
            ],
            options={
                'verbose_name': 'factura',
                'db_table': 'metropolitana_paquete',
                'managed': False,
                'verbose_name_plural': 'importacion de facturas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pod',
            fields=[
            ],
            options={
                'verbose_name': 'comprobante',
                'db_table': 'metropolitana_paquete',
                'managed': False,
                'verbose_name_plural': 'carga de imagenes manual',
            },
            bases=(models.Model,),
        ),
    ]
