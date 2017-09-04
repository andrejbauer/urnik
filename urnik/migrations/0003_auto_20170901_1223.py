# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urnik', '0002_auto_20170401_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='srecanje',
            name='dan',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'ponedeljek'), (2, 'torek'), (3, 'sreda'), (4, 'četrtek'), (5, 'petek')], null=True),
        ),
        migrations.AlterField(
            model_name='srecanje',
            name='ura',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]