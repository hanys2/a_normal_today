# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0004_auto_20181126_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.TextField(null=True),
        ),
    ]
