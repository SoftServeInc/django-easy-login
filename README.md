## Requirements
Python (3.5, 3.6, 3.7)
Django (1.11)

### Installation
...
Package not created yet.
--
Add 'easy_login' to your INSTALLED_APPS settings:
```
INSTALLED_APPS = [
    ...
    'easy_login',
]
```

Now edit the example/urls.py module in your project:
```
urlpatterns = [
    ...
    url(r'^easy_login/', include('easy_login.urls', namespace='easy-login')),
    ...
]
```

Set middleware class:
```
TEMPLATES = [
    ...
    'context_processors': [
        'easy_login.context_processors.easy_login',
        ...
    ],
]
```

Define default url redirect:
```
EASY_URL_REDIRECT = 'test-app:index'

```
In template define easy_login variable:
```
{{ easy_login }}
```
