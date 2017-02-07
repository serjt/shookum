# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-07 19:21
from __future__ import unicode_literals

from django.db import migrations, models
import subscribe.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration_date', models.DateField()),
                ('name', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to=subscribe.models.image_upload_to)),
                ('cover', models.ImageField(blank=True, null=True, upload_to=subscribe.models.image_upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('checked', models.BooleanField(default=False)),
            ],
        ),
    ]
