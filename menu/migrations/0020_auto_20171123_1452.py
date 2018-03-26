# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-23 14:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0019_auto_20171122_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='Pay_in_this_tri_1',
        ),
        migrations.RemoveField(
            model_name='person',
            name='Pay_in_this_tri_2',
        ),
        migrations.RemoveField(
            model_name='person',
            name='Pay_in_this_tri_3',
        ),
        migrations.RemoveField(
            model_name='person',
            name='Payment_in_this_trimester',
        ),
        migrations.AddField(
            model_name='cashvalue',
            name='Finance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.Finance'),
        ),
        migrations.AddField(
            model_name='cashvalue',
            name='Person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.Person'),
        ),
    ]