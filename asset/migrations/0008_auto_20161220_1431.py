# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-20 14:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0007_crontab_svn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gogroup',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='go group name'),
        ),
    ]
