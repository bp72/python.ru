# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-13 11:39
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20180113_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='language',
            field=models.CharField(choices=[('ru', '🇷🇺'), ('en', '🇬🇧')], max_length=2, verbose_name='Язык'),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', verbose_name='Текст'),
        ),
    ]