# Generated by Django 3.0.2 on 2020-02-16 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ncov', '0004_auto_20200216_1656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cnovhisinfo',
            old_name='cid',
            new_name='pid',
        ),
    ]
