# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View


class ViewHome(View):
    def get(self, request, *args, **kwargs):
        context = {'current_user': request.user}
        return render(request, "home.html", context=context)
