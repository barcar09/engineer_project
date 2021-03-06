# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-22 11:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0017_cashvalue_vat_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pay_in_this_month', models.BooleanField(default=False)),
                ('Pay_for_books', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='Payments',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='menu.MonthlyPayment'),
            preserve_default=False,
        ),
    ]
