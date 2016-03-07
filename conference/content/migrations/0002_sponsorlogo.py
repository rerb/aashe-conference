# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import feincms.module.medialibrary.fields


class Migration(migrations.Migration):

    dependencies = [
        ('medialibrary', '__first__'),
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SponsorLogo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=255)),
                ('url', models.TextField(max_length=255)),
                ('image', feincms.module.medialibrary.fields.MediaFileForeignKey(related_name='+', to='medialibrary.MediaFile')),
            ],
            options={
                'verbose_name': 'Sponsor Logo',
                'verbose_name_plural': 'Sponsor Logos',
            },
        ),
    ]
