# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import digitalizacion.models


class Migration(migrations.Migration):

    dependencies = [
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
                ('ecuenta', models.FileField(upload_to=digitalizacion.models.get_media_url, null=True, verbose_name=b'estado de cuenta', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Indexacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(auto_now_add=True, null=True)),
                ('carpeta', models.CharField(max_length=8, null=True)),
                ('make_ocr', models.BooleanField(default=False, verbose_name=b'hacer ocr')),
            ],
            options={
                'verbose_name': 'archivos pdf',
                'verbose_name_plural': 'carga de imagenes masiva',
            },
            bases=(models.Model,),
        ),
    ]
