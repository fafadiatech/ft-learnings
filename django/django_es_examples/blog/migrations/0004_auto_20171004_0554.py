# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 05:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cover_image',
            field=models.FileField(blank=True, default=None, null=True, upload_to='blog_cover_images'),
        ),
    ]
