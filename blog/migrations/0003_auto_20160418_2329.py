# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 02:29
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20160416_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colunista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('bio', models.TextField(help_text='Falar sobre o colunista')),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('imagem', models.ImageField(upload_to='')),
                ('texto', models.TextField()),
                ('slug', models.SlugField()),
                ('data_de_publicacao', models.DateTimeField(default=datetime.datetime(2016, 4, 19, 2, 28, 56, 481845, tzinfo=utc))),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Colunista')),
            ],
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='Categoria',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='title',
            new_name='titulo',
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='columnists',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='noticia',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Categoria'),
        ),
        migrations.AddField(
            model_name='colunista',
            name='categorias',
            field=models.ManyToManyField(to='blog.Categoria'),
        ),
        migrations.AddField(
            model_name='colunista',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='categoria',
            name='colunistas',
            field=models.ManyToManyField(to='blog.Colunista'),
        ),
    ]