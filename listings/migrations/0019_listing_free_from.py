# Generated by Django 3.1.3 on 2020-11-21 18:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0018_auto_20201121_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='free_from',
            field=models.DateField(blank=True, default=datetime.datetime.now, verbose_name='Free from'),
        ),
    ]
