# Generated by Django 3.0.2 on 2020-02-16 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ncov', '0002_zoneinfo_people'),
    ]

    operations = [
        migrations.CreateModel(
            name='CnovHisInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(default='0', max_length=64, verbose_name='区域序号')),
                ('confirmedNum', models.IntegerField(default=0, verbose_name='确诊人数')),
                ('curesNum', models.IntegerField(default=0, verbose_name='治愈人数')),
                ('deathsNum', models.IntegerField(default=0, verbose_name='死亡人数')),
                ('s_date', models.CharField(default='2020-01-01', max_length=64, verbose_name='日期')),
                ('bak', models.CharField(max_length=1023, verbose_name='备份')),
            ],
        ),
    ]
