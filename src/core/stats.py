""" Utility code for statistics.
"""

from awards.models import MatchAward


class MatchStats(object):
    """Represents statistics about a particular match"""

    def __init__(self, match):
        self.match = match
        self.scoring_appearances = []
        self.mom_winners = []
        self.lom_winners = []

    def add_appearance(self, appearance):
        """ Add the given appearance to the match stats."""
        if appearance.goals > 0:
            self.scoring_appearances.append(appearance)

    def add_award_winner(self, award_winner):
        """ Add the given award winner to the match stats. """
        if award_winner.award.name == MatchAward.MOM:
            self.mom_winners.append(award_winner)
        elif award_winner.award.name == MatchAward.LOM:
            self.lom_winners.append(award_winner)
