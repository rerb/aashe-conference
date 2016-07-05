# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_hostinstitutionlogo_hostinstitutionlogocollection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostinstitutionlogocollection',
            name='level',
            field=models.CharField(max_length=1028, verbose_name=b'Host/Sponsor Level', choices=[(b'Platinum', b'Platinum'), (b'Silver', b'Silver'), (b'Bronze', b'Bronze'), (b'Friend', b'Friend'), (b'Master', b'Master Host'), (b'Regional', b'Regional Host'), (b'Supporting', b'Supporting Host')]),
        ),
    ]
