# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import feincms.module.medialibrary.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0015_auto_20160705_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostinstitutionlogo',
            name='image',
            field=feincms.module.medialibrary.fields.MediaFileForeignKey(related_name='+', verbose_name=b'Logo Image', to='medialibrary.MediaFile', null=True),
        ),
        migrations.AlterField(
            model_name='hostinstitutionlogo',
            name='url',
            field=models.TextField(max_length=255, null=True, blank=True),
        ),
    ]
