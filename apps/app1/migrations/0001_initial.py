# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_reg_app', '0002_auto_20161118_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('published', models.CharField(max_length=55)),
                ('datefrom', models.CharField(max_length=40)),
                ('dateto', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('going', models.ManyToManyField(related_name='trips', to='login_reg_app.User')),
            ],
        ),
    ]