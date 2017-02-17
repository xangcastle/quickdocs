# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_auto_20170127_1617'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expediente',
            options={'verbose_name': 'Documento', 'verbose_name_plural': 'Expediente'},
        ),
    ]
