# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-26 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xmpp_http_upload', '0002_auto_20150913_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='type',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
