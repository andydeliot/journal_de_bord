# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_de_bord', '0007_auto_20170801_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='souvenir',
            name='texte',
            field=models.CharField(max_length=1000),
        ),
    ]
