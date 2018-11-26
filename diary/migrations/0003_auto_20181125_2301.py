# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_auto_20181125_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo_thumbnail',
        ),
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
