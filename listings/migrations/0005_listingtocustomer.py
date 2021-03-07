# Generated by Django 3.1.3 on 2020-11-14 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20201113_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListingToCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='listings.listing')),
            ],
        ),
    ]
