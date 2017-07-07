# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-07 19:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170707_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdatapoint',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 7, 19, 24, 13, 580125, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='itemdatapoint',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]