# Generated by Django 2.2.2 on 2019-06-08 22:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20190608_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 8, 22, 34, 3, 653752)),
        ),
    ]
