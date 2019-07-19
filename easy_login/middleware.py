import re

from django.utils.deprecation import MiddlewareMixin
from django.template.loader import render_to_string
from django.template import TemplateSyntaxError
from django.template.context_processors import csrf

from easy_login.forms import SwitchUserForm


class ShowPanelMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        content = response.content.decode(response.charset)
        insert_before = '</body>'
        pattern = re.escape(insert_before)
        bits = re.split(pattern, content, flags=re.IGNORECASE)
        if len(bits) > 1:
            bits[-2] += self.render_menu(request)
            response.content = insert_before.join(bits)
            if response.get("Content-Length", None):
                response["Content-Length"] = len(response.content)

        return response

    def render_menu(self, request):
        """
        Renders the Menu.
        """
        context = {}
        context.update(csrf(request))
        if request.user.is_authenticated:
            form = SwitchUserForm(initial={'user': request.user.id})
        else:
            form = SwitchUserForm()
        context['form'] = form

        try:
            return render_to_string("base.html", context)
        except TemplateSyntaxError:
            raise
