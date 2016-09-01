# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0017_auto_20160901_1504'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deadline',
            options={'ordering': ('order', 'pk'), 'verbose_name': 'Deadline', 'verbose_name_plural': 'Deadlines'},
        ),
        migrations.AddField(
            model_name='deadline',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
