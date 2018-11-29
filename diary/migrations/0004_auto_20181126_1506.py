# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_auto_20181125_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.TextField(),
        ),
    ]
