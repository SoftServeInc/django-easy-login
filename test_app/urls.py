from django.conf.urls import url

from test_app.views import ViewHome

urlpatterns = [
    url('^test/$',  ViewHome.as_view(), name='index')
]