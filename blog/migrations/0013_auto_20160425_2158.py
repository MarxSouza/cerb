# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 00:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20160425_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='data_de_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 26, 0, 58, 12, 889100, tzinfo=utc), verbose_name='Data de Publicação'),
        ),
    ]