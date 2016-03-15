# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import feincms.module.medialibrary.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_sponsorlogo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorlogo',
            name='image',
            field=feincms.module.medialibrary.fields.MediaFileForeignKey(related_name='+', verbose_name=b'Logo Image', to='medialibrary.MediaFile'),
        ),
        migrations.AlterField(
            model_name='sponsorlogo',
            name='name',
            field=models.TextField(max_length=255, verbose_name=b'Sponsor Name'),
        ),
        migrations.AlterField(
            model_name='sponsorlogo',
            name='url',
            field=models.TextField(max_length=255, verbose_name=b'Link URL'),
        ),
    ]
