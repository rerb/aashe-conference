# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20160315_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogoCollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=25)),
                ('images', models.ManyToManyField(to='content.SponsorLogo')),
            ],
            options={
                'verbose_name': 'Logo Collection',
            },
        ),
    ]
