# Generated by Django 2.2.2 on 2019-06-14 21:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20190608_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 14, 21, 14, 42, 537235)),
        ),
    ]