# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-12 21:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20171112_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group_type',
            name='group_time',
        ),
    ]
