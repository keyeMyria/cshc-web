# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 08:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import image_cropping.fields
import teams.models.participation


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20171007_1455'),
        ('competitions', '0002_auto_20171006_1844'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubTeamSeasonParticipation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_photo', django_resized.forms.ResizedImageField(blank=True, crop=None, keep_meta=True, null=True, quality=0, size=[900, 600], upload_to=teams.models.participation.get_file_name, verbose_name='Team photo')),
                ('cropping', image_cropping.fields.ImageRatioField('team_photo', '900x600', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping')),
                ('team_photo_caption', models.TextField(blank=True)),
                ('final_pos', models.PositiveSmallIntegerField(blank=True, default=None, help_text='Once the season is complete, enter the final league position here', null=True, verbose_name='Final position')),
                ('division_result', models.CharField(blank=True, choices=[('Promoted', 'Promoted'), ('Relegated', 'Relegated'), ('Champions', 'Champions')], default=None, help_text='Set to one of the options if the team was promoted or relegated this season.', max_length=20, null=True)),
                ('division_tables_url', models.URLField(blank=True, verbose_name='League table website')),
                ('division_fixtures_url', models.URLField(blank=True, verbose_name='Fixtures website')),
                ('cup_result', models.CharField(blank=True, default=None, help_text='Where did the team get to in the cup? (Enter once cup participation is complete)', max_length=100, null=True, verbose_name='Cup result')),
                ('blurb', models.TextField(blank=True)),
                ('friendly_played', models.PositiveSmallIntegerField(default=0, verbose_name='Friendly games played')),
                ('friendly_won', models.PositiveSmallIntegerField(default=0, verbose_name='Friendly games won')),
                ('friendly_drawn', models.PositiveSmallIntegerField(default=0, verbose_name='Friendly games drawn')),
                ('friendly_lost', models.PositiveSmallIntegerField(default=0, verbose_name='Friendly games lost')),
                ('friendly_goals_for', models.PositiveSmallIntegerField(default=0, verbose_name='Friendly goals for')),
                ('friendly_goals_against', models.PositiveSmallIntegerField(default=0, verbose_name='Friendly goals against')),
                ('cup_played', models.PositiveSmallIntegerField(default=0, verbose_name='Cup games played')),
                ('cup_won', models.PositiveSmallIntegerField(default=0, verbose_name='Cup games won')),
                ('cup_drawn', models.PositiveSmallIntegerField(default=0, verbose_name='Cup games drawn')),
                ('cup_lost', models.PositiveSmallIntegerField(default=0, verbose_name='Cup games lost')),
                ('cup_goals_for', models.PositiveSmallIntegerField(default=0, verbose_name='Cup goals for')),
                ('cup_goals_against', models.PositiveSmallIntegerField(default=0, verbose_name='Cup goals against')),
                ('league_played', models.PositiveSmallIntegerField(default=0, verbose_name='League games played')),
                ('league_won', models.PositiveSmallIntegerField(default=0, verbose_name='League games won')),
                ('league_drawn', models.PositiveSmallIntegerField(default=0, verbose_name='League games drawn')),
                ('league_lost', models.PositiveSmallIntegerField(default=0, verbose_name='League games lost')),
                ('league_goals_for', models.PositiveSmallIntegerField(default=0, verbose_name='League goals for')),
                ('league_goals_against', models.PositiveSmallIntegerField(default=0, verbose_name='League goals against')),
                ('cup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='competitions.Cup')),
                ('division', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='competitions.Division')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.Season')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.ClubTeam')),
            ],
        ),
        migrations.CreateModel(
            name='Southerner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('won', models.PositiveSmallIntegerField(default=0, verbose_name='Total number of games won')),
                ('drawn', models.PositiveSmallIntegerField(default=0, verbose_name='Total number of games drawn')),
                ('lost', models.PositiveSmallIntegerField(default=0, verbose_name='Total number of games lost')),
                ('goals_for', models.PositiveSmallIntegerField(default=0, verbose_name='Goals For')),
                ('goals_against', models.PositiveSmallIntegerField(default=0, verbose_name='Goals Against')),
                ('result_points', models.PositiveSmallIntegerField(default=0, verbose_name='Result points')),
                ('bonus_points', models.SmallIntegerField(default=0, verbose_name='Bonus points')),
                ('avg_points_per_game', models.FloatField(editable=False, verbose_name='Average points per game')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.Season')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.ClubTeam')),
            ],
            options={
                'ordering': ['season', 'avg_points_per_game'],
            },
        ),
        migrations.CreateModel(
            name='TeamCaptaincy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_vice', models.BooleanField(default=False, help_text='Check if this member is the vice captain (as opposed to the captain)', verbose_name='Vice-captain?')),
                ('start', models.DateField(help_text='The date this member took over as captain', verbose_name='Start of captaincy')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Member')),
                ('season', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='competitions.Season')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.ClubTeam')),
            ],
            options={
                'verbose_name_plural': 'team captaincy',
                'ordering': ['-start'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='southerner',
            unique_together=set([('team', 'season')]),
        ),
        migrations.AlterUniqueTogether(
            name='clubteamseasonparticipation',
            unique_together=set([('team', 'season')]),
        ),
    ]
