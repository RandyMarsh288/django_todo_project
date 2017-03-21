# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('1', 'Todo'), ('2', 'Doing'), ('3', 'Done')], max_length=1)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
