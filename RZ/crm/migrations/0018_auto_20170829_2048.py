# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-08-29 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0017_auto_20170829_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseinfo',
            name='zd_j',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='在贷金额'),
        ),
    ]
