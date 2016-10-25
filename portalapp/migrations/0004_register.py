# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portalapp', '0003_auto_20161003_1844'),
    ]

    operations = [
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
                ('image', models.ImageField(help_text='Maximum resolution 800x600. Larger images will be resized.', upload_to='photos')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
