# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 11:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opposition', '0001_initial'),
        ('teams', '0001_initial'),
        ('competitions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DivisionResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveSmallIntegerField()),
                ('played', models.PositiveSmallIntegerField(default=0)),
                ('won', models.PositiveSmallIntegerField(default=0)),
                ('drawn', models.PositiveSmallIntegerField(default=0)),
                ('lost', models.PositiveSmallIntegerField(default=0)),
                ('goals_for', models.PositiveSmallIntegerField(default=0)),
                ('goals_against', models.PositiveSmallIntegerField(default=0)),
                ('goal_difference', models.SmallIntegerField(default=0)),
                ('points', models.PositiveSmallIntegerField(default=0)),
                ('notes', models.TextField(blank=True, help_text='E.g. C for champion, P for promoted, R for relegated')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.Division')),
                ('opp_team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='opposition.Team')),
                ('our_team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.ClubTeam')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.Season')),
            ],
            options={
                'ordering': ('season', 'division', 'position'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='divisionresult',
            unique_together=set([('season', 'division', 'position')]),
        ),
    ]
