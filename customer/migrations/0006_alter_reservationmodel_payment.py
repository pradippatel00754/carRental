# Generated by Django 4.2 on 2023-04-20 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_alter_reservationmodel_r_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationmodel',
            name='payment',
            field=models.IntegerField(),
        ),
    ]
