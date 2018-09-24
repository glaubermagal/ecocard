# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from .views import virtualcard


urlpatterns = [
    url(r'^$', virtualcard, name='index'),
]