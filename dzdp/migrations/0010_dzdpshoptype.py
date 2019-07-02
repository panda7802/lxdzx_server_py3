# Generated by Django 2.2.2 on 2019-06-28 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dzdp', '0009_dzdpshop_shop_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='DzdpShopType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bak', models.CharField(blank=True, default='', max_length=1023, verbose_name='备份')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dzdp.DzdpShop')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dzdp.DzdpType')),
            ],
        ),
    ]
