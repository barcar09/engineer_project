# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-19 13:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0013_remove_person_count_of_payment_in_trimester'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Count_of_persons',
        ),
    ]