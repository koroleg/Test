# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_menuitem_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='has_children',
            field=models.BooleanField(default=False),
        ),
    ]
