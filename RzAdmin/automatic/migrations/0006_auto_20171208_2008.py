# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-08 12:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('automatic', '0005_auto_20171208_1722'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='downloadrecord',
            options={'verbose_name_plural': '下载记录表'},
        ),
        migrations.AlterModelOptions(
            name='sqlfunc',
            options={'verbose_name_plural': 'sql具备的功能表'},
        ),
        migrations.AlterModelOptions(
            name='sqlrecord',
            options={'verbose_name_plural': 'sql记录表'},
        ),
        migrations.AlterModelOptions(
            name='sqltag',
            options={'verbose_name_plural': 'sql标签表'},
        ),
    ]