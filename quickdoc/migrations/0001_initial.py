# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import quickdoc.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(max_length=25, null=True)),
                ('documento', models.FileField(null=True, upload_to=quickdoc.models.get_media_url, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=10, null=True, verbose_name=b'Codigo del Cliente')),
                ('identificacion', models.CharField(max_length=30, null=True, verbose_name=b'No de Identificacion')),
                ('nombre', models.CharField(max_length=150, null=True, verbose_name=b'Nombre Completo')),
                ('tipodoc', models.CharField(max_length=50, null=True, verbose_name=b'Tipo Documento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Indice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('indice', models.CharField(max_length=6)),
                ('descripcion', models.CharField(max_length=75)),
                ('indice_superior', models.ForeignKey(related_name=b'relacion_indice_superior', blank=True, to='quickdoc.Indice', null=True)),
            ],
            options={
                'ordering': ('indice',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='documento',
            name='expediente',
            field=models.ForeignKey(to='quickdoc.Expediente', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='indice',
            field=models.ForeignKey(to='quickdoc.Indice', null=True),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='indice_inferior',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('quickdoc.indice',),
        ),
        migrations.CreateModel(
            name='indice_intermedio',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('quickdoc.indice',),
        ),
        migrations.CreateModel(
            name='indice_superior',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('quickdoc.indice',),
        ),
    ]
