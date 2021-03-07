# Generated by Django 3.1.3 on 2020-11-16 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_auto_20201116_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listing_for',
            field=models.CharField(choices=[('R', 'Rent'), ('S', 'Sell')], default='S', max_length=5),
        ),
        migrations.DeleteModel(
            name='ListingFile',
        ),
    ]