# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('push_notifications', '0006_webpushdevice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apnsdevice',
            name='registration_id',
            field=models.CharField(max_length=200, unique=False, verbose_name='Registration ID'),
        ),
    ]
