# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 22:55
from __future__ import unicode_literals

from django.db import migrations, models
import journal_de_bord.models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_de_bord', '0006_auto_20170801_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journee',
            name='jour',
            field=models.DateField(default=journal_de_bord.models.aujourdhui, unique=True),
        ),
    ]
