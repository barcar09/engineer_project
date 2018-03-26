# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-22 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0018_auto_20171122_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='Payments',
        ),
        migrations.AddField(
            model_name='person',
            name='Pay_for_books',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='Pay_in_this_month',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='MonthlyPayment',
        ),
    ]
