""" Configuration of Match models for the admin interface.
"""

from django.contrib import admin
from django.forms import ModelForm, widgets
from awards.models import MatchAwardWinner
from .models import Match, Appearance
from .forms import MatchAdminForm


class MatchAwardWinnerInlineForm(ModelForm):
    """Inline form for match award winners"""

    class Meta:
        """ Meta-info for the form."""
        model = MatchAwardWinner
        exclude = [],


class MatchAwardWinnerInline(admin.TabularInline):
    """Inline for match award winners - allows quick editing of award winners in a match"""

    model = MatchAwardWinner
    form = MatchAwardWinnerInlineForm
    extra = 2
    verbose_name_plural = 'Award winners'


class AppearanceInlineForm(ModelForm):
    """Inline form for appearances"""

    class Meta:
        """ Meta-info for the form."""
        model = Appearance
        exclude = ['own_goals']
        widgets = {
            'green_card': widgets.NullBooleanSelect(attrs={'class': 'input-small'}),
            'yellow_card': widgets.NullBooleanSelect(attrs={'class': 'input-small'}),
            'red_card': widgets.NullBooleanSelect(attrs={'class': 'input-small'}),
        }


class AppearanceInline(admin.TabularInline):
    """Inline for appearances - allows quick editing of appearances in a match"""
    model = Appearance
    form = AppearanceInlineForm
    extra = 11
    verbose_name_plural = 'Appearances'
    exclude = ['own_goals']


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    """Model Admin for matches"""
    form = MatchAdminForm
    inlines = (
        MatchAwardWinnerInline,
        AppearanceInline,
    )
    radio_fields = {'fixture_type': admin.HORIZONTAL,
                    'home_away': admin.HORIZONTAL,
                    'alt_outcome': admin.HORIZONTAL}
    fieldsets = [
        ('Teams', {'fields': ['our_team', 'opp_team']}),
        ('Fixture details', {'fields': [
            'venue', 'home_away', 'fixture_type', 'date', 'time']}),
        ('Result', {'fields': ['alt_outcome', 'our_score', 'opp_score', 'our_ht_score',
                               'opp_ht_score']}),
        ('Advanced', {'classes': ('collapse',),
                      'fields': ['ignore_for_goal_king', 'ignore_for_southerners',
                                 'override_kit_clash', 'gpg_pro_rata']}),
        ('Pre-match hype', {
            'classes': ('full-width',),
            'fields': ['pre_match_hype']}),

        ('Match report', {
            'classes': ('full-width',),
            'fields': ['report_title', 'report_author', 'report_body']}),
    ]
    list_display = ('__str__', 'date', 'our_team', 'opp_team', 'venue')
    search_fields = ('our_team__long_name',
                     'our_team__short_name', 'opp_team__name', 'venue__name')
    list_filter = ('our_team', 'opp_team', 'venue',
                   'fixture_type', 'home_away', 'season')


@admin.register(Appearance)
class AppearanceAdmin(admin.ModelAdmin):
    """ Admin interface definition for the Appearance model."""

    model = Appearance
    search_fields = ('member__first_name',
                     'member__known_as', 'member__last_name')
    list_filter = ('green_card', 'yellow_card', 'red_card')


# NOTE: We do not register the GoalKing model - this is derived from other models
# and should never be edited via the admin interface
