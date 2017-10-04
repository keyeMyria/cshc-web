# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClubTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=10, unique=True)),
                ('long_name', models.CharField(max_length=100, unique=True)),
                ('gender', models.CharField(choices=[('M', 'Mens'), ('L', 'Ladies'), ('ML', 'Mixed')], max_length=6, verbose_name='Team gender (mens/ladies)')),
                ('ordinal', models.CharField(choices=[('T1', '1sts'), ('T2', '2nds'), ('T3', '3rds'), ('T4', '4ths'), ('T5', '5ths'), ('T6', '6ths'), ('T7', '7ths'), ('T8', '8ths'), ('T9', '9ths'), ('T10', '10ths'), ('T11', '11ths'), ('T12', '12ths'), ('TVets', 'Vets'), ('TIndoor', 'Indoor'), ('TOther', 'Other')], max_length=10, verbose_name='Team ordinal (1sts/2nds etc)')),
                ('position', models.PositiveSmallIntegerField(help_text='Used to order the teams for display', unique=True)),
                ('southerners', models.BooleanField(default=True, help_text='Include in Southerners League stats')),
                ('rivals', models.BooleanField(default=True, help_text='Include in Rivals stats')),
                ('fill_blanks', models.BooleanField(default=True, help_text='Show blank fixture dates')),
                ('personal_stats', models.BooleanField(default=True, help_text='Use for personal stats')),
                ('active', models.BooleanField(default=True, help_text='Uncheck if this team is not currently active')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('blurb', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['position'],
            },
        ),
    ]
