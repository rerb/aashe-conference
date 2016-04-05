# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_headerboxcontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=128)),
            ],
            options={
                'verbose_name': 'Benefit',
                'verbose_name_plural': 'Benefits',
            },
        ),
        migrations.CreateModel(
            name='RegistrationLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level_name', models.TextField(max_length=128, verbose_name=b'Name')),
                ('price', models.DecimalField(verbose_name=b'Registration Price', max_digits=10, decimal_places=2)),
                ('checks', models.ManyToManyField(to='content.Benefit', verbose_name=b'Included Benefits (boxes to check off)')),
            ],
            options={
                'verbose_name': 'Registration Level',
                'verbose_name_plural': 'Registration Levels',
            },
        ),
    ]
