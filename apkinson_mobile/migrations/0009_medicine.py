# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-08-19 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apkinson_mobile', '0008_auto_20190818_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicinename', models.CharField(max_length=40)),
                ('dose', models.IntegerField(default='2')),
                ('intaketime', models.IntegerField(default='0')),
                ('id_name', models.CharField(max_length=40)),
            ],
        ),
    ]
