# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-24 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171221_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, help_text='用来作为SEO中description,长度参考SEO标准', max_length=240, null=True, verbose_name='描述'),
        ),
        migrations.AddField(
            model_name='tag',
            name='description',
            field=models.TextField(blank=True, help_text='用来作为SEO中description,长度参考SEO标准', max_length=240, null=True, verbose_name='描述'),
        ),
    ]
