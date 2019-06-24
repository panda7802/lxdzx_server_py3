# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 13:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video_manager', '0007_auto_20171202_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='People_Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bak_data', models.CharField(blank=True, default='', max_length=1024, verbose_name='\u5907\u7528\u5b57\u6bb5')),
                ('people_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video_manager.People')),
                ('video_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video_manager.Video')),
            ],
        ),
    ]