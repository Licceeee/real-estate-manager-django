# Generated by Django 3.1.3 on 2020-11-21 17:54

import datetime
from django.db import migrations, models
import django.db.models.deletion
import listings.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20201121_1854'),
        ('core', '0002_auto_20201121_1854'),
        ('listings', '0014_auto_20201118_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='address',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.address', verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bathrooms',
            field=models.PositiveIntegerField(verbose_name='Bathrooms'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bedrooms',
            field=models.PositiveIntegerField(verbose_name='Bedrooms'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='ceiling_height',
            field=models.FloatField(blank=True, null=True, verbose_name='Ceiling height'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='garage',
            field=models.IntegerField(default=0, verbose_name='Garage'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(upload_to=listings.models.listing_dir_path, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='listing_for',
            field=models.CharField(choices=[('S', 'Sell'), ('R', 'Rent')], default='S', max_length=5, verbose_name='Listing for'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='listing_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='listings.listingtype', verbose_name='Listing type'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='lot_size',
            field=models.FloatField(verbose_name='Lot size'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='realtor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.realtor', verbose_name='Realtor'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='sqft',
            field=models.FloatField(verbose_name='sqft'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Updated'),
        ),
        migrations.AlterField(
            model_name='listingimage',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='listingimage',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=listings.models.listing_dir_path, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='listingimage',
            name='listing',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='listings.listing', verbose_name='Listing'),
        ),
        migrations.AlterField(
            model_name='listingimage',
            name='short_description',
            field=models.CharField(max_length=255, verbose_name='Short description'),
        ),
    ]
