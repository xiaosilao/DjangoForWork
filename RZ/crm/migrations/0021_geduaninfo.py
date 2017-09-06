# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-09-05 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0020_auto_20170831_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeDuanInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qdate', models.DateField(db_index=True, verbose_name='日期')),
                ('geduan', models.CharField(max_length=32, verbose_name='各端类型')),
                ('recover', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='各端已还')),
                ('recover_withdraw', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='各端回款并提现')),
                ('account', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='各端投资')),
                ('xztz_j', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='各端新增投资')),
                ('withdraw', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='各端提现金额')),
            ],
            options={
                'verbose_name': '各端数据',
                'verbose_name_plural': '各端数据',
            },
        ),
    ]