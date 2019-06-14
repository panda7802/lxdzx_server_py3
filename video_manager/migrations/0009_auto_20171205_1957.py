# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 19:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video_manager', '0008_people_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='parent_tag_id',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='video_manager.Tag'),
        ),
    ]
