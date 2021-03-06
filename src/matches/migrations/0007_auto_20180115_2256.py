# Generated by Django 2.0.1 on 2018-01-15 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0006_auto_20180110_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goalking',
            name='vets_goals',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Goals for the Vets team'),
        ),
        migrations.AlterField(
            model_name='goalking',
            name='vets_own_goals',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Own goals for the Vets team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='opp_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='opposition.Team', verbose_name='Opposition team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='our_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teams.ClubTeam', verbose_name='Our team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='season',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to='competitions.Season'),
        ),
    ]
