# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-22 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='tema',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='projeto',
            name='titulo',
            field=models.CharField(default='', max_length=100),
        ),
    ]