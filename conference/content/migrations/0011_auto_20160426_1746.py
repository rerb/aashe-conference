# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_auto_20160406_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderimage',
            name='button_link_1',
            field=models.TextField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='button_link_2',
            field=models.TextField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='sponsorlogo',
            name='url',
            field=models.TextField(max_length=255),
        ),
    ]
