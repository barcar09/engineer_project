# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-26 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0022_auto_20171125_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group_in_time',
            name='Time_minutes',
            field=models.IntegerField(),
        ),
    ]