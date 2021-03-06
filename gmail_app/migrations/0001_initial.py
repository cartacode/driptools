# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-09-16 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_username', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('from_email', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('to_email', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('subject', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('preview_text', models.TextField(blank=True, default='', null=True)),
                ('body_text', models.TextField(blank=True, default='', null=True)),
                ('day_of_week', models.IntegerField(blank=True, null=True)),
                ('time_of_day', models.TimeField(blank=True, null=True)),
                ('image_count', models.IntegerField(blank=True, null=True)),
                ('subject_word_count', models.IntegerField(blank=True, null=True)),
                ('preview_word_count', models.IntegerField(blank=True, null=True)),
                ('body_word_count', models.IntegerField(blank=True, null=True)),
                ('date_sent', models.DateField(blank=True, default='')),
            ],
        ),
    ]
