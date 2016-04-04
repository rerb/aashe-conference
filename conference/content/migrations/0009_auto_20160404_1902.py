# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_headerboxcontent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headerboxcontent',
            name='content',
        ),
        migrations.AddField(
            model_name='headerboxcontent',
            name='text_line_1',
            field=models.TextField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='headerboxcontent',
            name='text_line_2',
            field=models.TextField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='headerboxcontent',
            name='title',
            field=models.TextField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
