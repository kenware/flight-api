# Generated by Django 2.2.2 on 2019-06-08 17:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flight', '0003_auto_20190608_1735'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2019, 6, 8, 17, 35, 46, 653201))),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=250)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('flight_date', models.DateField()),
                ('flight_seat', models.CharField(max_length=255)),
                ('ref', models.CharField(default='j2fQODFj0RChtL1Cw2VR2gmM9kf6yTX5', max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flights', to='flight.Flight')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
