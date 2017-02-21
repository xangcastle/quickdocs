# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0006_proveedor_pago_anual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='identificacion',
            field=models.CharField(max_length=24, verbose_name=b'RUC/CEDULA'),
        ),
    ]
