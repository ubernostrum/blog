# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-26 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_populate_updated_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='updated_date',
            field=models.DateTimeField(blank=True, editable=False),
        ),
    ]