from django.conf.urls import url

from test_app.views import ViewHome

urlpatterns = [
    url('^$',  ViewHome.as_view(), name='index')
]