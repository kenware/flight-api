# Generated by Django 2.2.2 on 2019-06-14 21:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20190608_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 14, 21, 14, 42, 537235)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='ref',
            field=models.CharField(default='8lASA502skbiIpS5ZZMFLMgHFDMBw1Sg', max_length=255),
        ),
    ]