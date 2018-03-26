# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-14 17:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_auto_20171114_1731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group_in_time',
            old_name='Exactly_time',
            new_name='Time_hour',
        ),
        migrations.AddField(
            model_name='group_in_time',
            name='Time_day',
            field=models.CharField(default=django.utils.timezone.now, max_length=220),
            preserve_default=False,
        ),
    ]