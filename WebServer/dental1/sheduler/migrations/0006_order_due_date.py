# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-23 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0005_auto_20170416_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='due_date',
            field=models.DateTimeField(null=True, verbose_name='order due date'),
        ),
    ]
