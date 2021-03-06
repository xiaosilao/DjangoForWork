# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-02 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0045_delete_tgqudaoname'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyAssetInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qdate', models.DateField(db_index=True, verbose_name='日期')),
                ('term', models.CharField(max_length=32, verbose_name='期限类型')),
                ('tz_r', models.IntegerField(verbose_name='投资人数')),
                ('tz_j', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='投资金额')),
                ('mb_ys', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='满标用时')),
                ('asset_type', models.CharField(default='所有', max_length=32, verbose_name='资产类型')),
            ],
            options={
                'verbose_name': '日报资产数据',
                'verbose_name_plural': '日报资产数据',
                'db_table': 'rzjf_daily_asset_info',
            },
        ),
    ]
