# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0002_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='author',
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
