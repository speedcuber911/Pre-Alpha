# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-14 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0011_auto_20160413_2128'),
    ]

    operations = [
        migrations.DeleteModel(
            name='question',
        ),
        migrations.AddField(
            model_name='coach_profile',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]