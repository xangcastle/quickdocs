# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecuenta', '0007_auto_20170207_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paquete',
            name='entregado',
            field=models.BooleanField(default=False),
        ),
    ]
