# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 04:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0003_auto_20170409_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_out',
            field=models.DateTimeField(null=True, verbose_name='order date out'),
        ),
    ]
