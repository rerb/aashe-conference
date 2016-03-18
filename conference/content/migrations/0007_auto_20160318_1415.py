# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_logocollection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderimage',
            name='button_link_1',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='button_link_2',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='button_text_1',
            field=models.TextField(max_length=15, blank=True),
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='button_text_2',
            field=models.TextField(max_length=15, blank=True),
        ),
    ]
