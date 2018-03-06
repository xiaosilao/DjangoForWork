# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-05 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0057_lossrate'),
    ]

    operations = [
        migrations.AddField(
            model_name='recasting',
            name='one_month_ft_j',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='本月首投用户复投金额'),
        ),
        migrations.AddField(
            model_name='recasting',
            name='one_month_ft_lv',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='本月首投用户复投率'),
        ),
        migrations.AddField(
            model_name='recasting',
            name='one_month_ft_r',
            field=models.IntegerField(null=True, verbose_name='本月首投后复投人数'),
        ),
        migrations.AddField(
            model_name='recasting',
            name='one_month_st_r',
            field=models.IntegerField(null=True, verbose_name='本月首投人数'),
        ),
        migrations.AddField(
            model_name='recasting',
            name='two_month_ft_j',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='前两月首投用户复投金额'),
        ),
        migrations.AddField(
            model_name='recasting',
            name='two_month_ft_lv',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='前两月首投用户复投率'),
        ),
        migrations.AddField(
            model_name='recasting',
            name='two_month_ft_r',
            field=models.IntegerField(null=True, verbose_name='前两月首投后复投人数'),
        ),
        migrations.AddField(
            model_name='recasting',
            name='two_month_st_r',
            field=models.IntegerField(null=True, verbose_name='前两月首投人数'),
        ),
    ]