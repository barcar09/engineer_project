# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-14 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_auto_20171114_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group_in_time',
            name='Exactly_time',
            field=models.CharField(max_length=220),
        ),
    ]