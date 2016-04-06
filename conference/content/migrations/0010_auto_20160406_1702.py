# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_benefit_registrationlevel'),
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
        migrations.RemoveField(
            model_name='registrationlevel',
            name='checks',
        ),
        migrations.RemoveField(
            model_name='registrationlevel',
            name='price',
        ),
        migrations.AddField(
            model_name='registrationlevel',
            name='first_deadline_price',
            field=models.IntegerField(default=0, verbose_name=b'First Deadline Price'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrationlevel',
            name='level_details',
            field=models.TextField(max_length=256, verbose_name=b'Details', blank=True),
        ),
        migrations.AddField(
            model_name='registrationlevel',
            name='on_site_price',
            field=models.IntegerField(default=0, verbose_name=b'On-Site Price'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrationlevel',
            name='second_deadline_price',
            field=models.IntegerField(default=0, verbose_name=b'Second Deadline Price'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrationlevel',
            name='third_deadline_price',
            field=models.IntegerField(default=0, verbose_name=b'Third Deadline Price'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Benefit',
        ),
    ]
