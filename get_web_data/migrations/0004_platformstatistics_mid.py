# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-05 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_web_data', '0003_auto_20180905_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='platformstatistics',
            name='mid',
            field=models.IntegerField(default=0, verbose_name='\u5e8f\u53f7'),
        ),
    ]
