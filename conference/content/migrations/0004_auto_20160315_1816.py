# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20160315_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='sliderimage',
            name='button_link_1',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sliderimage',
            name='button_link_2',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sliderimage',
            name='button_text_1',
            field=models.TextField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sliderimage',
            name='button_text_2',
            field=models.TextField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sliderimage',
            name='text_header_line_1',
            field=models.TextField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sliderimage',
            name='text_header_line_2',
            field=models.TextField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sliderimage',
            name='text_block',
            field=models.TextField(max_length=150),
        ),
    ]
