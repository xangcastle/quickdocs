# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0003_nuevo_sectorizacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectorizacion',
            name='nuevo',
            field=models.ForeignKey(to='compras.nuevo', null=True),
            preserve_default=True,
        ),
    ]
