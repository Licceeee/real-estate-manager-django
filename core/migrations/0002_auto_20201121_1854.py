# Generated by Django 3.1.3 on 2020-11-21 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Country', 'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'verbose_name': 'State', 'verbose_name_plural': 'States'},
        ),
        migrations.RemoveField(
            model_name='address',
            name='test',
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=100, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='address',
            name='hn',
            field=models.CharField(max_length=15, verbose_name='House number'),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.state', verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=150, verbose_name='Street'),
        ),
        migrations.AlterField(
            model_name='address',
            name='zipcode',
            field=models.CharField(max_length=5, verbose_name='Zipcode'),
        ),
        migrations.AlterField(
            model_name='state',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.country', verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Country'),
        ),
    ]
