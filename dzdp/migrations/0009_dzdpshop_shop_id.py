# Generated by Django 2.2.2 on 2019-06-19 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dzdp', '0008_auto_20190618_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='dzdpshop',
            name='shop_id',
            field=models.CharField(blank=True, default='', max_length=1023, verbose_name='商店号'),
        ),
    ]