# Generated by Django 5.0.2 on 2024-02-24 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_hotelvendor_business_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hoteluser',
            options={},
        ),
        migrations.AlterModelOptions(
            name='hotelvendor',
            options={},
        ),
        migrations.AlterModelTable(
            name='hoteluser',
            table='hotel_user',
        ),
        migrations.AlterModelTable(
            name='hotelvendor',
            table='hotel_vendor',
        ),
    ]