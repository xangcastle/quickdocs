# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_auto_20170210_0504'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='utilidad',
            field=models.FloatField(default=b'0.0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articulo',
            name='costo',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='descuento',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='precio',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='total',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]
