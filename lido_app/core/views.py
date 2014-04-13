# Core app views.
import logging

from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    """Site homepage - shows the temp chart."""
    logger.debug(u"%s is viewing the homepage.", request.user)
    return render(request, 'index.html')
