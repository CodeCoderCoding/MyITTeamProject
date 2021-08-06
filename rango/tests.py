import os
import re
import rango.models
from rango import forms
from populate_rango import populate
from datetime import datetime, timedelta
from django.db import models
from django.test import TestCase
from django.conf import settings
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.forms import fields as django_fields

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"

f"{FAILURE_HEADER} {FAILURE_FOOTER}"


class Chapter10ConfigurationTests(TestCase):
    """
    Tests the configuration of the Django project -- can cookies be used, at least on the server-side?
    """

    def test_middleware_present(self):
        """
        Tests to see if the SessionMiddleware is present in the project configuration.
        """
        self.assertTrue('django.contrib.sessions.middleware.SessionMiddleware' in settings.MIDDLEWARE)

    def test_session_app_present(self):
        """
        Tests to see if the sessions app is present.
        """
        self.assertTrue('django.contrib.sessions' in settings.INSTALLED_APPS)


class Chapter10SessionPersistenceTests(TestCase):
    """
    Tests to see if session data is persisted by counting up the number of accesses, and examining last time since access.
    """

    def test_visits_counter(self):
        """
        Tests the visits counter.
        Artificially tweaks the last_visit variable to force a counter increment.
        """
        for i in range(0, 10):
            response = self.client.get(reverse('rango:home'))
            session = self.client.session

            self.assertIsNotNone(session['visits'])
            self.assertIsNotNone(session['last_visit'])

            # Get the last visit, and subtract one day.
            # Forces an increment of the counter.
            last_visit = datetime.now() - timedelta(days=1)

            session['last_visit'] = str(last_visit)
            session.save()

            self.assertEquals(session['visits'], i + 1)