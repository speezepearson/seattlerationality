# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lightning_talks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lightningtalk',
            name='embed_video_html',
            field=models.CharField(max_length=4095),
        ),
        migrations.AlterField(
            model_name='lightningtalk',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
