# Generated by Django 3.1.3 on 2020-11-16 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_auto_20201116_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listing_for',
            field=models.CharField(choices=[('S', 'Sell'), ('R', 'Rent')], default='S', max_length=5),
        ),
    ]
