# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-15 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_remove_image_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='gallery/'),
        ),
    ]
