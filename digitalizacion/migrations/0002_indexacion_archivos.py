# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multifilefield.models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalizacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexacion',
            name='archivos',
            field=multifilefield.models.MultiFileField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
