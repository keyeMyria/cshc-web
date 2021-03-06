""" The TeamCaptaincy model tracks who was captain (and vice-captain)
    of a particular CSHC team in a particular season.
"""

from django.db import models


class TeamCaptaincyManager(models.Manager):
    """ Queries relating to the TeamCaptaincy model. """

    def get_queryset(self):
        return super(TeamCaptaincyManager, self).get_queryset().select_related('member', 'team', 'season')

    def by_team(self, team):
        """ Returns only entries for the specified team. """
        return self.get_queryset().filter(team=team)

    def by_member(self, member):
        """ Returns only entries for the specified member. """
        return self.get_queryset().filter(member=member)

    def by_season(self, season):
        """ Returns only entries for the specified season. """
        return self.get_queryset().filter(season=season)

    def captains(self):
        """ Returns only captains (as opposed to vice-captains). """
        return self.get_queryset().filter(is_vice=False)

    def vice_captains(self):
        """ Returns only vice-captains (as opposed to captains). """
        return self.get_queryset().filter(is_vice=True)


class TeamCaptaincy(models.Model):
    """ Represents a member's term as captain/vice-captain of a team"""

    member = models.ForeignKey('members.Member', on_delete=models.CASCADE)

    team = models.ForeignKey('teams.ClubTeam', on_delete=models.CASCADE)

    is_vice = models.BooleanField("Vice-captain?", default=False,
                                  help_text="Check if this member is the vice captain (as opposed to the captain)")
    """True if this is a vice-captaincy role"""

    start = models.DateField("Start of captaincy",
                             help_text="The date this member took over as captain")
    """The date that the member started their captaincy"""

    season = models.ForeignKey(
        'competitions.Season', on_delete=models.SET_NULL, null=True, blank=True)

    objects = TeamCaptaincyManager()

    class Meta:
        """ Meta-info for the TeamCaptaincy model. """
        app_label = 'teams'
        verbose_name_plural = 'team captaincy'
        ordering = ['-start']

    def __str__(self):
        return str("{} {}: {}".format(self.team, self.role(), self.member))

    def role(self):
        """ Returns a string representation of the player's role - either
            'captain' or 'vice-captain'.
        """
        return "vice-captain" if self.is_vice else "captain"

    @staticmethod
    def get_captains(team, season):
        """ Returns TeamCaptaincy objects corresponding to the captains for
            the specified team and season.
        """
        return TeamCaptaincy.objects.by_team(team=team).by_season(season).captains()

    @staticmethod
    def get_vice_captains(team, season):
        """ Returns TeamCaptaincy objects corresponding to the vice captains for
            the specified team and season.
        """
        return TeamCaptaincy.objects.by_team(team).by_season(season).vice_captains()
