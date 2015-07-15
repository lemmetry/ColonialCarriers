# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_description', models.TextField(max_length=250)),
                ('additional_information', models.TextField(max_length=250)),
                ('facility', models.ForeignKey(to='partners.Facility', blank=True)),
            ],
        ),
    ]
