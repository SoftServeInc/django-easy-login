# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from easy_login.forms import SwitchUserForm
from django.contrib.auth import login
from django.views.generic.base import View


class SwitchUserView(View):
    form_class = SwitchUserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            if user is not None:
                login(request, user)

        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
