# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from django.conf import settings
from gmail_app import views


urlpatterns = [
    url(r'^dashboard/', views.dashboard, name="gmail_dashboard"),
    url(r'^emails/', views.get_emails_by_from, name="get_emails_by_from"),
]
