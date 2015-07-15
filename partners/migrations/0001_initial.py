# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('street_address', models.CharField(max_length=200)),
                ('city', models.CharField(default=b'Williamsburg', max_length=25)),
                ('state', models.CharField(default=b'VA', max_length=2)),
                ('zip', models.CharField(default=b'23185', max_length=5)),
                ('phone_number', models.CharField(max_length=10)),
                ('fax_number', models.CharField(max_length=10, blank=True)),
                ('homepage', models.URLField(blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=10, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='facility',
            name='manager',
            field=models.ForeignKey(to='partners.Manager', blank=True),
        ),
    ]
