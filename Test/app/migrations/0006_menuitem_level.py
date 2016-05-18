# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_menuitem_has_children'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='level',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
