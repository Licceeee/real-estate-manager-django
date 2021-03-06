# Generated by Django 3.1.3 on 2020-11-13 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('shortcut', models.CharField(max_length=3, verbose_name='ISO 3166-α2')),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('shortcut', models.CharField(max_length=6, verbose_name='ISO 3166-2')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.country')),
            ],
            options={
                'verbose_name_plural': 'States',
                'unique_together': {('country', 'shortcut')},
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=150)),
                ('hn', models.CharField(max_length=15)),
                ('zipcode', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=100)),
                ('test', models.IntegerField()),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.state')),
            ],
            options={
                'verbose_name_plural': 'Addresses',
                'unique_together': {('street', 'hn', 'zipcode')},
            },
        ),
    ]
