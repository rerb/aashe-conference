# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_auto_20160426_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='deadline',
            name='strikethrough',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
