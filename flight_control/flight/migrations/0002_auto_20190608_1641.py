# Generated by Django 2.2.2 on 2019-06-08 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 8, 16, 41, 23, 188392)),
        ),
        migrations.AlterField(
            model_name='flight',
            name='tag',
            field=models.CharField(default='TAATCAGAAGATGCCGTAGA', max_length=255),
        ),
    ]
