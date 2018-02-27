# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import leads.validators
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('gender', models.CharField(max_length=1, choices=[('m', 'male'), ('f', 'female')])),
                ('card_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Only numbers and capital letters: X, T, W are allowed', regex='^XTW[0-9]{8,15}$')], null=True, unique=True, blank=True)),
                ('expiry_date', models.DateField(validators=[leads.validators.date_validator], null=True, blank=True)),
                ('professional', models.CharField(max_length=1, choices=[('y', 'yes'), ('n', 'no')])),
            ],
        ),
        migrations.AddField(
            model_name='language',
            name='lead',
            field=models.ForeignKey(to='leads.Lead', related_name='languages'),
        ),
        migrations.AlterUniqueTogether(
            name='language',
            unique_together=set([('name', 'lead')]),
        ),
    ]
