# Generated by Django 3.1.3 on 2020-11-13 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListingFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(blank=True, default=None, null=True, upload_to='listings/files')),
                ('short_description', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('for_customer', models.BooleanField(default=True)),
                ('listing', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='listings.listing')),
            ],
        ),
    ]