# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-29 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentapplication',
            name='title',
            field=models.CharField(default='student applied', max_length=255),
            preserve_default=False,
        ),
    ]
