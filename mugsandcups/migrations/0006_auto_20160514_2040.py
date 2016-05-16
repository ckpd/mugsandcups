# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-15 00:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mugsandcups', '0005_delete_cupssection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('client_logo', models.FileField(upload_to='')),
                ('data_categories', models.CharField(max_length=250)),
                ('src', models.CharField(max_length=200)),
                ('alt', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]