# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-26 03:14
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_begin_updated_date'),
    ]

    operations = [
        migrations.RunSQL(
            ["UPDATE blog_entry SET updated_date = pub_date;"],
            migrations.RunSQL.noop
        )
    ]