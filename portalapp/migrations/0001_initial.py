# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Maximum 250 characters.', max_length=250, blank=True)),
                ('slug', models.SlugField(help_text='Suggested value automatically generated from title. Must be unique.', unique=True, null=True)),
                ('caption', models.TextField(help_text='An optional summary.', max_length=250, blank=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('image', models.ImageField(help_text='Maximum resolution 800x600. Larger images will be resized.', upload_to='photos')),
                ('album', models.CharField(default='ALL', max_length=6, choices=[('ALL', 'All'), ('CAMPUS', 'Campus'), ('CULT', 'Cult'), ('ACADS', 'Acads')])),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='PressRelease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(max_length=256)),
                ('summary', models.TextField(help_text='A summary for the archive.', blank=True)),
                ('slug', models.SlugField(help_text='Suggested value automatically generated from title. Must be unique.', unique=True, null=True)),
                ('content', tinymce.models.HTMLField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=200)),
                ('abstract', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('speaker', models.CharField(max_length=200)),
                ('venue', models.CharField(max_length=200)),
                ('date_and_time', models.DateTimeField(default=datetime.datetime.now)),
                ('bio', models.TextField()),
                ('coordinator', models.CharField(max_length=200)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
