# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='gender',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female')], default='m', max_length=1),
        ),
        migrations.AlterField(
            model_name='lead',
            name='professional',
            field=models.CharField(choices=[('y', 'yes'), ('n', 'no')], default='y', max_length=1),
        ),
    ]
