# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-03 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to=b'')),
                ('text', models.TextField()),
            ],
        ),
    ]