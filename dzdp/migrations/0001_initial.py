# Generated by Django 2.2.2 on 2019-06-17 15:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DzdpCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1023, verbose_name='名称')),
                ('tag', models.CharField(max_length=1023, verbose_name='标签')),
                ('province', models.CharField(max_length=1023, verbose_name='省份')),
                ('country', models.CharField(max_length=1023, verbose_name='省份')),
                ('bak', models.CharField(default=False, max_length=1023, verbose_name='备份')),
            ],
        ),
        migrations.CreateModel(
            name='DzdpType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1023, verbose_name='名称')),
                ('curr_page', models.IntegerField(default=0, verbose_name='当前爬取的页面')),
                ('is_max_page', models.BooleanField(default=False, verbose_name='是否最大页面')),
                ('bak', models.CharField(default=False, max_length=1023, verbose_name='备份')),
            ],
        ),
        migrations.CreateModel(
            name='DzdpShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1023, verbose_name='名称')),
                ('price', models.FloatField(default=0, verbose_name='价格')),
                ('pic', models.IntegerField(default=0, verbose_name='图片')),
                ('good', models.IntegerField(default=0, verbose_name='好评')),
                ('common', models.IntegerField(default=0, verbose_name='中评')),
                ('bad', models.IntegerField(default=0, verbose_name='差评')),
                ('phone', models.CharField(max_length=64, verbose_name='电话')),
                ('url', models.CharField(max_length=1023, verbose_name='url')),
                ('lon', models.FloatField(default=0, verbose_name='经度')),
                ('lat', models.FloatField(default=0, verbose_name='纬度')),
                ('lastGetTime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='上次爬取时间')),
                ('bak', models.CharField(default=False, max_length=1023, verbose_name='备份')),
                ('type_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dzdp.DzdpType')),
            ],
        ),
    ]
