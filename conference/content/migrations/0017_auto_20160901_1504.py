# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0016_auto_20160706_2018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registrationlevel',
            options={'ordering': ('order', 'pk'), 'verbose_name': 'Registration Level', 'verbose_name_plural': 'Registration Levels'},
        ),
        migrations.AddField(
            model_name='registrationlevel',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
