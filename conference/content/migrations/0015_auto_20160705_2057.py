# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0014_auto_20160705_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostinstitutionlogocollection',
            name='level',
            field=models.CharField(max_length=1028, verbose_name=b'Host/Sponsor Level', choices=[(b'Platinum', b'Platinum'), (b'Gold', b'Gold'), (b'Silver', b'Silver'), (b'Bronze', b'Bronze'), (b'Friend', b'Friend'), (b'Master', b'Master Host'), (b'Regional', b'Regional Host'), (b'Supporting', b'Supporting Host')]),
        ),
    ]
