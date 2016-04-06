# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_auto_20160406_1702'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Deadline',
        ),
        migrations.DeleteModel(
            name='RegistrationLevel',
        ),
    ]
