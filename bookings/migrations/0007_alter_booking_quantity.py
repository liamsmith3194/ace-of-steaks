# Generated by Django 3.2 on 2022-03-09 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0006_auto_20220308_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='quantity',
            field=models.IntegerField(choices=[(1, 'One'), (2, 'Two')], verbose_name='Number of Guests'),
        ),
    ]
