# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-24 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0002_delete_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('body', models.TextField()),
                ('date', models.DateField()),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
