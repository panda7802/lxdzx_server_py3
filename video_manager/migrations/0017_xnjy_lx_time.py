# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-24 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_manager', '0016_auto_20171224_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='xnjy',
            name='lx_time',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='\u5bc4\u8bed'),
        ),
    ]
