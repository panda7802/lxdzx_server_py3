# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-07 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_web_data', '0008_auto_20180905_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platformstatistics',
            name='clicks',
            field=models.BigIntegerField(default=0, verbose_name='\u603b\u70b9\u51fb\u91cf'),
        ),
        migrations.AlterField(
            model_name='platformstatistics',
            name='fans',
            field=models.BigIntegerField(default=0, verbose_name='\u603b\u7c89\u4e1d\u6570'),
        ),
        migrations.AlterField(
            model_name='platformstatistics',
            name='follows',
            field=models.BigIntegerField(default=0, verbose_name='\u5173\u6ce8\u6570'),
        ),
        migrations.AlterField(
            model_name='platformstatistics',
            name='reads',
            field=models.BigIntegerField(default=0, verbose_name='\u9605\u8bfb\u6570'),
        ),
    ]
