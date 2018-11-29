# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-28 03:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20181128_0248'),
    ]

    operations = [
        migrations.CreateModel(
            name='IDCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_num', models.CharField(max_length=40)),
                ('i_sex', models.CharField(max_length=8)),
                ('i_addr', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=80)),
                ('p_age', models.IntegerField()),
            ],
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('myObjects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='idcard',
            name='i_person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Person'),
        ),
    ]
