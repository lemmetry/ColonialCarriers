# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0003_auto_20150531_1928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='date',
            new_name='time_stamp',
        ),
        migrations.AlterField(
            model_name='item',
            name='additional_information',
            field=models.CharField(max_length=250, blank=True),
        ),
    ]
