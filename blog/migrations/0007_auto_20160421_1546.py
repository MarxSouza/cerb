# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 18:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160421_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colunista',
            name='nome',
        ),
        migrations.AlterField(
            model_name='noticia',
            name='data_de_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 21, 18, 46, 13, 48705, tzinfo=utc), verbose_name='Data de Publicação'),
        ),
    ]