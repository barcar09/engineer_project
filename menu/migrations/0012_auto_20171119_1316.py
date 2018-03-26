# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-19 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0011_auto_20171114_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Count_of_persons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Trimester_type', models.CharField(max_length=220)),
                ('Pay_in_this_tri', models.SmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='Count_of_payment_in_trimester',
            field=models.ManyToManyField(related_name='menu_person_related', related_query_name='menu_persons', to='menu.Finance'),
        ),
        migrations.AddField(
            model_name='person',
            name='Payment_in_this_trimester',
            field=models.ManyToManyField(to='menu.Finance'),
        ),
    ]