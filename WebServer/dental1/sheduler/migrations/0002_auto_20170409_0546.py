# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-09 05:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderPrinted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('num_doc', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Printed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_process_start', models.DateTimeField()),
                ('date_process_end', models.DateTimeField()),
                ('printed_order_status', models.IntegerField()),
                ('status', models.IntegerField(choices=[(1, 'New'), (2, 'InProcess'), (3, 'Ended')], default=1)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='cost',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='sheduler.Doctor'),
        ),
        migrations.AlterField(
            model_name='order',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheduler.Patient'),
        ),
        migrations.AddField(
            model_name='orderprinted',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheduler.Order'),
        ),
        migrations.AddField(
            model_name='orderprinted',
            name='printed_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheduler.Printed'),
        ),
    ]
