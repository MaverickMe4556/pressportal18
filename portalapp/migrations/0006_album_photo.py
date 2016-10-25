# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0005_delete_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('image', models.ImageField(upload_to='photos')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Maximum 250 characters.', max_length=250, blank=True)),
                ('slug', models.SlugField(help_text='Suggested value automatically generated from title. Must be unique.', unique=True, null=True)),
                ('caption', models.TextField(help_text='An optional summary.', max_length=250, blank=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('image', models.ImageField(help_text='Maximum resolution 800x600. Larger images will be resized.', upload_to='photos')),
                ('album', models.ForeignKey(to='portalapp.Album')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
