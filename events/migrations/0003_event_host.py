# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 02:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('events', '0002_auto_20171122_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='host',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]
