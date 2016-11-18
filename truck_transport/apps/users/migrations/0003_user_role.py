# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-17 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20161025_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, b'Provider'), (2, b'Driver'), (3, b'Broker')], null=True, verbose_name='Role'),
        ),
    ]