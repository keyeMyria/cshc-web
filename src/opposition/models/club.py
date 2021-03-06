""" The Club model represents an opposition hockey club.

    Note that Cambridge South also features as an 'opposition' club
    as we frequently have matches against other teams in our club.
"""

from django.db import models
from django.template.defaultfilters import slugify
from core.models import TeamGender
from venues.models import Venue


class Club(models.Model):
    """Represents an opposition club"""
    # The club name
    name = models.CharField("Club Name", max_length=255,
                            unique=True, default=None)

    # The club website (if it has one)
    website = models.URLField("Club Website", blank=True)

    # Indicates whether this club's men's kit currently clashes with our men's kit
    kit_clash_men = models.BooleanField("Kit-clash (men)", default=False,
                                        help_text="Does this club's mens kit clash with our mens kit?")

    # Indicates whether this club's ladies kit currently clashes with our ladies kit
    kit_clash_ladies = models.BooleanField("Kit-clash (ladies)", default=False,
                                           help_text="Does this club's ladies kit clash with our ladies kit?")

    # Indicates whether this club's mixed team's kit currently clashes with our mixed team's kit
    kit_clash_mixed = models.BooleanField("Kit-clash (mixed)", default=False,
                                          help_text="Does this club's mixed team kit clash with our mixed team kit?")

    # The default venue for this club, if known
    default_venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True,
                                      help_text="The venue this club usually plays at (if known)")

    # Auto-generated slug - used in the url for club details
    slug = models.SlugField("Slug")

    class Meta:
        """ Meta-info for the Club model."""
        app_label = 'opposition'
        ordering = ['name']

    def clean(self):
        self.slug = slugify(self.name)

    def __str__(self):
        return str(self.name)

    @models.permalink
    def get_absolute_url(self):
        """ Returns the url for this club instance."""
        return ('opposition_club_detail', [self.slug])

    def kit_clash(self, team_gender):
        """Returns true if, for the specified team gender, this club's kit clashes with our kit"""
        if team_gender == TeamGender.Mens:
            return self.kit_clash_men
        elif team_gender == TeamGender.Ladies:
            return self.kit_clash_ladies
        elif team_gender == TeamGender.Mixed:
            return self.kit_clash_mixed

        raise AssertionError("Unexpected team gender")
