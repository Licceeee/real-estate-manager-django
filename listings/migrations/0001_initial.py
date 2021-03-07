# Generated by Django 3.1.3 on 2020-11-13 15:32

import datetime
from django.db import migrations, models
import django.db.models.deletion
import listings.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('ceiling_height', models.FloatField(blank=True, null=True)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('garage', models.IntegerField(default=0)),
                ('sqft', models.FloatField()),
                ('lot_size', models.FloatField()),
                ('image', models.ImageField(upload_to=listings.models.listing_dir_path)),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('address', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.address')),
            ],
        ),
        migrations.CreateModel(
            name='ListingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ListingImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to=listings.models.listing_dir_path)),
                ('short_description', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('listing', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='listings.listing')),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='listing_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='listings.listingtype'),
        ),
        migrations.AddField(
            model_name='listing',
            name='realtor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.realtor'),
        ),
    ]