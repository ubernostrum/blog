# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=markupfield.fields.MarkupField(rendered_field=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='body',
            field=markupfield.fields.MarkupField(rendered_field=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='excerpt',
            field=markupfield.fields.MarkupField(rendered_field=True, blank=True, null=True),
        ),
    ]
