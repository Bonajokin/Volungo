# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]