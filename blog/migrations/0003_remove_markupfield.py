# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_markupfield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='entry',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='entry',
            name='excerpt',
            field=models.TextField(null=True, blank=True),
        ),
    ]
