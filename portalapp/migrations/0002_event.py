# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(max_length=256)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('venue', models.CharField(max_length=512)),
                ('content', models.TextField()),
                ('image', models.ImageField(help_text='Maximum resolution 800x600. Larger images will be resized.', upload_to='eventphotos')),
            ],
        ),
    ]
