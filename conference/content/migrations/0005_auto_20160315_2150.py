# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20160315_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorlogo',
            name='url',
            field=models.URLField(),
        ),
    ]
