from easy_login.forms import SwitchUserForm
from django.template.context_processors import csrf
from django.template.loader import render_to_string


def easy_login(request):
    context = {}
    context.update(csrf(request))
    context['form'] = SwitchUserForm(initial={'user': request.user.id})
    render_page = render_to_string("base.html", context)

    return {"easy_login": render_page}
