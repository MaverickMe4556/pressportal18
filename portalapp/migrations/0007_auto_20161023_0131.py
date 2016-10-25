# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0006_album_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PressRelease',
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(help_text='Can also use garbage images', upload_to='eventphotos'),
        ),
    ]
