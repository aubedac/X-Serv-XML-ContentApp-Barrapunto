# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-17 16:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contentAppBarraPunto', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pages',
            old_name='content',
            new_name='page',
        ),
    ]
