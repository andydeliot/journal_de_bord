# Generated by Django 2.0.5 on 2018-05-02 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal_de_bord', '0005_auto_20180502_0353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journee',
            name='dure',
        ),
    ]