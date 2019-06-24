# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 11:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video_manager', '0005_auto_20171125_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='parent_tag_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='video_manager.Tag'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='cost_time',
            field=models.IntegerField(default=0, verbose_name='\u65f6\u957f(\u79d2)'),
        ),
    ]