# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView, View


class ViewHome(TemplateView):
    template_name = 'home.html'
