# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-27 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automatic', '0007_auto_20180226_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='download_status',
            field=models.BooleanField(default=False, verbose_name='是否拥有下载权限'),
        ),
    ]
