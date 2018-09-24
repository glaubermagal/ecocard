# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView


class VirtualCardView(TemplateView):
    template_name = 'virtualcard/index.html'


virtualcard = VirtualCardView.as_view()