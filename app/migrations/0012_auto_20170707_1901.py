# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-07 19:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20170707_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdatapoint',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 7, 19, 1, 52, 405560, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='itemdatapoint',
            name='itemID',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='itemdatapoint',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
