# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_menu_menuitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='level',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='parent',
        ),
        migrations.AddField(
            model_name='menu',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2016, 5, 18, 7, 50, 6, 823013, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.CharField(max_length=100),
        ),
    ]
