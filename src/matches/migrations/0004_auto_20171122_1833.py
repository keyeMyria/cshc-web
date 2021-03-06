# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-22 11:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0003_auto_20171009_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='goalking',
            name='gpg',
            field=models.FloatField(editable=False, null=True, verbose_name='Goals per Game'),
        ),
        migrations.AddField(
            model_name='goalking',
            name='mpg',
            field=models.FloatField(editable=False, null=True, verbose_name='Miles per Game'),
        ),
        migrations.AlterField(
            model_name='match',
            name='venue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matches', to='venues.Venue'),
        ),
    ]
