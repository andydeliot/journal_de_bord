# Generated by Django 2.0.5 on 2018-08-06 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_de_bord', '0007_journee_dure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journee',
            name='dure',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
