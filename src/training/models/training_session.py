""" A model that represents a particular training session.

    Also used for 'Pay and Play' sessions.

    All sessions have a description, a start time and duration (in minutes)
    and are associated with a Venue. The status of previously scheduled
    venues can be set to 'Cancelled' to show that a particular session has
    been cancelled (rather than just deleting it).
"""

from django.utils import timezone
from django.db import models
from django.db.models.query import QuerySet
from venues.models import Venue
from competitions.models import Season


class TrainingSessionStatus(object):
    """ Enumeration of possible statuses for training sessions """
    Scheduled = 'Scheduled'
    Cancelled = 'Cancelled'
    Choices = (
        ('Scheduled', 'Scheduled'),
        ('Cancelled', 'Cancelled'),
    )


class TrainingSessionManager(models.Manager):
    """TrainingSession model manager"""

    def get_queryset(self):
        return super(TrainingSessionManager, self).get_queryset().select_related('venue')

    def upcoming(self):
        """Returns only training sessions in the future, sorted by date"""
        return self.get_queryset().filter(datetime__gte=timezone.now()).order_by('datetime')

    def before(self, dt):
        """ Returns all training sessions scheduled prior to the specified date/time."""
        return self.get_queryset().filter(datetime__lt=dt).order_by('datetime')

    def this_season(self):
        """Returns only training sessions for this season"""
        season = Season.current()
        return self.get_queryset().filter(datetime__gte=season.start, datetime__lte=season.end).order_by('datetime')


class TrainingSession(models.Model):
    """Represents a training session"""

    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    """The venue where the training session takes place"""

    description = models.CharField(
        max_length=100, default='Full club training')
    """The type of training session"""

    datetime = models.DateTimeField("Training date/time")
    """The start time (and date) of the training session"""

    duration_mins = models.PositiveSmallIntegerField(
        "Duration (minutes)", default=120)
    """The duration, in minutes, of the training session"""

    status = models.CharField(
        'Status', max_length=20, choices=TrainingSessionStatus.Choices, default=TrainingSessionStatus.Scheduled)
    """The status of the training session (e.g. cancelled/scheduled)"""

    objects = TrainingSessionManager()

    class Meta:
        """ Meta-info for the TrainingSession model."""
        app_label = 'training'
        ordering = ['datetime']
        # Ensure we don't create 'identical' two sessions
        unique_together = ('description', 'datetime')

    def __str__(self):
        return "{} ({})".format(self.description, self.datetime)

    @models.permalink
    def get_absolute_url(self):
        """ Returns the url for this training session."""
        return ('trainingsession_detail', [self.pk])
