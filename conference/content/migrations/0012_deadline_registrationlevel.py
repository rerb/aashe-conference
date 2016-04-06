# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_auto_20160406_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deadline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deadline', models.TextField(max_length=128)),
            ],
            options={
                'verbose_name': 'Deadline',
                'verbose_name_plural': 'Deadlines',
            },
        ),
        migrations.CreateModel(
            name='RegistrationLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level_name', models.TextField(max_length=128, verbose_name=b'Name')),
                ('level_details', models.TextField(max_length=256, verbose_name=b'Details', blank=True)),
                ('first_deadline_price', models.IntegerField(verbose_name=b'First Deadline Price')),
                ('second_deadline_price', models.IntegerField(verbose_name=b'Second Deadline Price')),
                ('third_deadline_price', models.IntegerField(verbose_name=b'Third Deadline Price')),
                ('on_site_price', models.IntegerField(verbose_name=b'On-Site Price')),
            ],
            options={
                'verbose_name': 'Registration Level',
                'verbose_name_plural': 'Registration Levels',
            },
        ),
    ]
