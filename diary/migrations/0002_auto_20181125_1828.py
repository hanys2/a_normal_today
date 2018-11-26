# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='photo_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='/static/upload'),
        ),
        migrations.AddField(
            model_name='post',
            name='singer',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='song',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
