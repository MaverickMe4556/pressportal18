# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0004_register'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
