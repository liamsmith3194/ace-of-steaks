# Generated by Django 3.2 on 2022-03-09 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0008_alter_booking_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='mobile',
        ),
        migrations.AlterField(
            model_name='booking',
            name='location',
            field=models.CharField(choices=[('LOND', 'London'), ('GLAS', 'Glasgow'), ('CARD', 'Cardiff')], max_length=50, verbose_name='Restuarant Location'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='quantity',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=50, verbose_name='Number of Guests'),
        ),
    ]