# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0004_auto_20150531_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='time_stamp',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True),
        ),
    ]
