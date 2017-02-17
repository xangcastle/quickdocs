# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecuenta', '0004_auto_20170207_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='paquete',
            name='entregado_temp',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
