# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_trafictimes_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='RushHour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
                ('rush_hour', models.BooleanField(default=False)),
            ],
        ),
    ]
