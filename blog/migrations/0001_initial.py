# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 05:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(choices=[('Educação', 'Educação'), ('Esporte', 'Esporte'), ('Moda', 'Moda'), ('Política', 'Política'), ('Tecnologia', 'Tecnologia'), ('Saúde', 'Saúde'), ('Fatos Corriqueiros', 'Fatos Corriqueiros'), ('Música', 'Música')], max_length=100, verbose_name='Título')),
                ('slug', models.SlugField()),
                ('colunista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='noticias')),
                ('autor', models.CharField(max_length=200)),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('texto', models.TextField()),
                ('views', models.PositiveIntegerField(default=0)),
                ('data_de_publicacao', models.DateTimeField(verbose_name='Data de Publicação')),
                ('slug', models.SlugField()),
                ('categoria', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Categoria')),
            ],
        ),
    ]
