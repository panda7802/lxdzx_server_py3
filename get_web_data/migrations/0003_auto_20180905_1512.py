# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-05 15:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get_web_data', '0002_platformstatistics'),
    ]

    operations = [
        migrations.RenameField(
            model_name='platformstatistics',
            old_name='title',
            new_name='bak',
        ),
        migrations.RemoveField(
            model_name='platformstatistics',
            name='plays',
        ),
    ]
