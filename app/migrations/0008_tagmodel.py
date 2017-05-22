# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-22 23:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20170518_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='tagModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
                ('tutorials', models.ManyToManyField(to='app.tutorialModel')),
            ],
        ),
    ]
