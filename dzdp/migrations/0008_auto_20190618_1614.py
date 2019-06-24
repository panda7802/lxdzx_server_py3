# Generated by Django 2.2.2 on 2019-06-18 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dzdp', '0007_auto_20190618_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dzdptype',
            name='curr_page',
        ),
        migrations.RemoveField(
            model_name='dzdptype',
            name='is_max_page',
        ),
        migrations.CreateModel(
            name='DzdpCityType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curr_page', models.IntegerField(default=0, verbose_name='当前爬取的页面')),
                ('is_max_page', models.BooleanField(default=False, verbose_name='是否最大页面')),
                ('bak', models.CharField(blank=True, default='', max_length=1023, verbose_name='备份')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dzdp.DzdpCity')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dzdp.DzdpType')),
            ],
        ),
    ]