# Generated by Django 2.2.13 on 2021-08-05 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_parts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
