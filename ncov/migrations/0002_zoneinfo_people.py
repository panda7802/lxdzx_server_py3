# Generated by Django 2.2.3 on 2020-02-06 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ncov', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zoneinfo',
            name='people',
            field=models.IntegerField(default=0, max_length=64, verbose_name='人口'),
        ),
    ]
