# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import feincms.module.medialibrary.fields


class Migration(migrations.Migration):

    dependencies = [
        ('medialibrary', '__first__'),
        ('content', '0012_deadline_strikethrough'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostInstitutionLogo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=255, verbose_name=b'Sponsor Name')),
                ('url', models.TextField(max_length=255, blank=True)),
                ('image', feincms.module.medialibrary.fields.MediaFileForeignKey(related_name='+', verbose_name=b'Logo Image', blank=True, to='medialibrary.MediaFile')),
            ],
            options={
                'verbose_name': 'Host Institution/Sponsor Logo',
                'verbose_name_plural': 'Host Institution/Sponsor Logos',
            },
        ),
        migrations.CreateModel(
            name='HostInstitutionLogoCollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=25)),
                ('level', models.CharField(max_length=1028, verbose_name=b'Host/Sponsor Level', choices=[(b'platinum', b'Platinum'), (b'silver', b'Silver'), (b'bronze', b'Bronze'), (b'friend', b'Friend'), (b'master', b'Master Host'), (b'regional', b'Regional Host'), (b'supporting', b'Supporting Host')])),
                ('images', models.ManyToManyField(to='content.HostInstitutionLogo', blank=True)),
            ],
            options={
                'verbose_name': 'Host Institution/Sponsor Logo Collection',
            },
        ),
    ]
