# Generated by Django 3.2 on 2022-03-09 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0009_auto_20220309_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='location',
            field=models.CharField(choices=[('London', 'London'), ('Glasgow', 'Glasgow'), ('Cardiff', 'Cardiff')], max_length=50, verbose_name='Restuarant Location'),
        ),
    ]
