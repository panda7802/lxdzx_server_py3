# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-06 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_manager', '0012_auto_20171205_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='pic_url',
            field=models.FileField(blank=True, default='', upload_to=b'D:\\lxdzx\\lxdzx_server/static/files/recv', verbose_name='\u56fe\u7247'),
        ),
        migrations.AlterField(
            model_name='video',
            name='pic_url',
            field=models.FileField(blank=True, default='', upload_to=b'D:\\lxdzx\\lxdzx_server/static/files/recv', verbose_name='\u56fe\u7247'),
        ),
    ]
