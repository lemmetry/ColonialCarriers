# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0002_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='additional_information',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='item',
            name='facility',
            field=models.ForeignKey(to='partners.Facility'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_description',
            field=models.CharField(max_length=250),
        ),
    ]
