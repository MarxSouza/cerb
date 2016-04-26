# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 01:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20160425_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='visualizacoes',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='data_de_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 26, 1, 4, 45, 867589, tzinfo=utc), verbose_name='Data de Publicação'),
        ),
    ]