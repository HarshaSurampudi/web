# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-13 08:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_userprofileinfo_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='user',
            new_name='username',
        ),
    ]
