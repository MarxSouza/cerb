# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 00:33
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20160425_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='autor',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='data_de_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 26, 0, 33, 50, 497927, tzinfo=utc), verbose_name='Data de Publicação'),
        ),
    ]