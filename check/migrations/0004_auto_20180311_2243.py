# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-11 22:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0003_auto_20180311_1301'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usercheckdev',
            options={'ordering': ['-add_time'], 'verbose_name': '巡检信息', 'verbose_name_plural': '巡检信息'},
        ),
        migrations.AlterModelOptions(
            name='userchecksys',
            options={'ordering': ['-add_time'], 'verbose_name': '业务系统状态巡检', 'verbose_name_plural': '业务系统状态巡检'},
        ),
    ]