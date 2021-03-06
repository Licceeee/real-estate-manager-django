# Generated by Django 3.1.3 on 2020-11-21 17:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0015_auto_20201121_1854'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0006_remove_contact_outdated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Contact date'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='listings.listing', verbose_name='Listing'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(blank=True, verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=100, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
