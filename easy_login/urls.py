from django.conf.urls import url

from easy_login.views import SwitchUserView

urlpatterns = [
    url('^switch_user/$',  SwitchUserView.as_view(), name='switch-user')
]
