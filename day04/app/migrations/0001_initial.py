# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-29 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('color', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('run', models.CharField(max_length=100)),
                ('bark', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eat', models.CharField(max_length=100)),
            ],
        ),
    ]
