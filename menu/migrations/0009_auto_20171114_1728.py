# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-14 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_remove_group_in_time_group_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group_in_time',
            name='Exactly_time',
            field=models.TimeField(),
        ),
    ]
