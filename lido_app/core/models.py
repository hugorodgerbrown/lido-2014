# -*- coding: utf-8 -*-
import datetime
import logging

from django.contrib.auth.models import User
from django.db import models

logger = logging.getLogger(__name__)


class Measurement(models.Model):
    """A single temperature measurement, for a single day."""
    # the person who submitted the measurement.
    submitted_by = models.ForeignKey(User)
    # the date to which the measurement relates.
    date = models.DateField()
    # timestamp for when the measurement was received.
    created_at = models.DateTimeField()
    # the measurement itself - in Centigrade - supports 0.0 to 99.9
    temperature = models.DecimalField(max_digits=3, decimal_places=1)

    def __unicode__(self):
        return (
            u"Temperate recorded as %s on %s.",
            self.temperature,
            self.date
        )

    def __str__(self):
        return unicode(self).encode('utf-8')

    def save(self):
        """Sets the created_at timestamp if not set."""
        self.created_at = self.created_at or datetime.datetime.utcnow()
