# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import feincms.contrib.richtext


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0018_auto_20160901_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField(max_length=1024)),
                ('answer', feincms.contrib.richtext.RichTextField()),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQs',
            },
        ),
        migrations.CreateModel(
            name='FAQCollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('questions', models.ManyToManyField(to='content.FAQ')),
            ],
            options={
                'verbose_name': 'FAQ Collection',
            },
        ),
    ]
