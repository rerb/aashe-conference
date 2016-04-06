# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_deadline_registrationlevel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationlevel',
            name='level_details',
            field=models.TextField(max_length=512, verbose_name=b'Details', blank=True),
        ),
    ]
