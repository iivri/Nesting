# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-17 23:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nesting', '0004_auto_20171017_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identity_unique',
            name='First_Name',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='identity_unique',
            name='Last_Name',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]