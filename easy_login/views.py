# -*- coding: utf-8 -*-
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import login
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from easy_login.forms import SwitchUserForm


class EasyLoginView(View):
    form_class = SwitchUserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user_name']
            user_id = form.cleaned_data['user_id']

            if user:
                login(request, user)

            elif user_id:
                obj_user = get_object_or_404(User, pk=user_id)
                login(request, obj_user)

        if hasattr(settings, 'EASY_URL_REDIRECT'):
            url = reverse(settings.EASY_URL_REDIRECT)

            return HttpResponseRedirect(url)

        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
