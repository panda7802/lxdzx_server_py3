# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 20:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video_manager', '0009_auto_20171205_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='parent_tag_id',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='video_manager.Tag'),
        ),
    ]
