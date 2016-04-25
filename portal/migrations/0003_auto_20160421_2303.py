# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-22 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20160421_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='tema',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]