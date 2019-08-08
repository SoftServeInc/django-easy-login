from django.conf.urls import url

from easy_login.tests.test_app.views import ViewHome

urlpatterns = [
    url('^$',  ViewHome.as_view(), name='index')
]