# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_menuitem_level'),
    ]

    operations = [
        migrations.DeleteModel(
            name='JustBodyMessage',
        ),
    ]
