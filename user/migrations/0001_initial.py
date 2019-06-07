# Generated by Django 2.2.2 on 2019-06-07 00:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2019, 6, 7, 0, 21, 31, 896714))),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=250)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('image', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
