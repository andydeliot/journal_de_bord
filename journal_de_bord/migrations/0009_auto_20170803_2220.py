# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-03 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_de_bord', '0008_auto_20170802_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='souvenir',
            name='texte',
            field=models.CharField(max_length=10000),
        ),
    ]
