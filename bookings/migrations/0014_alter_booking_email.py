# Generated by Django 3.2 on 2022-03-13 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0013_alter_booking_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
    ]
