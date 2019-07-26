# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys

import django


def_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, def_path + '/../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_easy_login.settings")
django.setup()


from django.http import request
from easy_login.context_processors import easy_login
from django.contrib.auth.models import AnonymousUser
import django_easy_login.settings

django_easy_login.settings.SECRET_KEY = 'default_test_key'
django_easy_login.settings.ALLOWED_HOSTS = ["*"]


def test_form(monkeypatch):
    assert True


def test_easy_login(monkeypatch):
    request.user = None
    request.META = None
    monkeypatch.setattr(request, "user", AnonymousUser)
    monkeypatch.setattr(request, "META", {})
    render_page = easy_login(request)
    assert "easy_login" in render_page


def test_view(monkeypatch):
    assert True
