# Generated by Django 2.2.13 on 2021-08-05 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_parts', '0002_seller_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpart',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_parts.Seller'),
        ),
    ]
