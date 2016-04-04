# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20160318_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderBoxContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=25)),
                ('title', models.TextField(max_length=128)),
                ('text_line_1', models.TextField(max_length=128)),
                ('text_line_2', models.TextField(max_length=128)),
            ],
            options={
                'verbose_name': 'Header Box Content',
            },
        ),
    ]
