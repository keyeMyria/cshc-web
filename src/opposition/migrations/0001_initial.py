# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 08:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('venues', '0002_venue_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255, unique=True, verbose_name='Club Name')),
                ('website', models.URLField(blank=True, verbose_name='Club Website')),
                ('kit_clash_men', models.BooleanField(default=False, help_text="Does this club's mens kit clash with our mens kit?", verbose_name='Kit-clash (men)')),
                ('kit_clash_ladies', models.BooleanField(default=False, help_text="Does this club's ladies kit clash with our ladies kit?", verbose_name='Kit-clash (ladies)')),
                ('kit_clash_mixed', models.BooleanField(default=False, help_text="Does this club's mixed team kit clash with our mixed team kit?", verbose_name='Kit-clash (mixed)')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('default_venue', models.ForeignKey(help_text='The venue this club usually plays at (if known)', null=True, on_delete=django.db.models.deletion.CASCADE, to='venues.Venue')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Team name')),
                ('short_name', models.CharField(max_length=100, verbose_name='Abbreviated name')),
                ('gender', models.CharField(choices=[('M', 'Mens'), ('L', 'Ladies'), ('ML', 'Mixed')], max_length=6, verbose_name='Team gender (mens/ladies)')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='opposition.Club')),
            ],
            options={
                'ordering': ['club', 'name'],
            },
        ),
    ]
