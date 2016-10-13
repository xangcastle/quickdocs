# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cedula', models.CharField(max_length=14)),
                ('nombre', models.CharField(max_length=125, verbose_name=b'nombre completo')),
                ('moneda', models.CharField(default=b'DOLARES', max_length=20, choices=[(b'CORDOBAS', b'CORDOBAS'), (b'DOLARES', b'DOLARES')])),
                ('salario', models.FloatField(null=True)),
                ('tc', models.FloatField(default=1.0, null=True, verbose_name=b'tasa de cambio')),
                ('cuenta', models.CharField(help_text=b'cuenta banpro', max_length=25, null=True, verbose_name=b'cuenta a aplicar')),
                ('fecha_ingreso', models.DateField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Servicios Profesionales',
            },
            bases=(models.Model,),
        ),
    ]
