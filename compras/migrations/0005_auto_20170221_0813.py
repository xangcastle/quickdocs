# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0004_sectorizacion_nuevo'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='buro',
            field=models.CharField(max_length=165, null=True, verbose_name=b'calificacion de credito', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='proveedor',
            name='temp_user',
            field=models.CharField(max_length=125, null=True, blank=True),
            preserve_default=True,
        ),
    ]
