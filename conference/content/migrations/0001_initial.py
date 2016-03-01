# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import feincms.content.raw.models
import feincms.module.medialibrary.fields


class Migration(migrations.Migration):

    dependencies = [
        ('medialibrary', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text_block', models.TextField(verbose_name=feincms.content.raw.models.RawContent)),
                ('image', feincms.module.medialibrary.fields.MediaFileForeignKey(related_name='+', to='medialibrary.MediaFile')),
            ],
            options={
                'verbose_name': 'Image for master slider',
                'verbose_name_plural': 'Images for master slider',
            },
        ),
    ]
