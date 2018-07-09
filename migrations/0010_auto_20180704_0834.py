# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-03 22:34
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0009_auto_20180626_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_description',
            field=tinymce.models.HTMLField(verbose_name='project_description'),
        ),
        migrations.AlterField(
            model_name='project_history',
            name='project_history',
            field=tinymce.models.HTMLField(verbose_name='project_history'),
        ),
    ]