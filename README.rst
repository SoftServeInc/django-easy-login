=================
Django Easy Login
=================

Django Easy Login is a Django app that allows end-users to login with already created users at the system without
authentication.

Quick start
-----------

1. Add 'easy_login' to your INSTALLED_APPS settings::

    INSTALLED_APPS = [
    ...
    'easy_login',
    ]


2. Now edit the example/urls.py module in your project::

    urlpatterns = [
    ...
    url(r'^easy_login/', include('easy_login.urls', namespace='easy-login')),
    ...
    ]


3. Set middleware class::

    TEMPLATES = [
        ...
        'context_processors': [
            'easy_login.context_processors.easy_login',
            ...
        ],
    ]


4. Define default url redirect::

    EASY_URL_REDIRECT = 'test-app:index'


5. In template define easy_login variable::

    {{ easy_login }}
