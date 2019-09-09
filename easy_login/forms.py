from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

view_settings = {
    'FILTER': {},
    'LIMIT': 10,
    'LABELS': [],
    'LOGIN_BY': 'both',
    'GET_BY': 'pk',
    'LOGIN_BUTTON': 'Login'
}

if hasattr(settings, 'EASY_LOGIN_SETTINGS'):
    view_settings.update(settings.EASY_LOGIN_SETTINGS)


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        """
        Updated function to show labels according to the settings
        """
        if view_settings['LABELS'] and type(view_settings['LABELS']) is list:
            labels = []
            for attr in view_settings['LABELS']:
                labels.append(str(getattr(obj, attr)))
            label = ', '.join(labels)
        elif callable(view_settings['LABELS']):
            label = view_settings['LABELS'](obj)
        else:
            label = obj
        return '{}'.format(label)


class EasyLoginForm(forms.Form):
    user_name = MyModelChoiceField(queryset=User.objects.none(), required=False)
    placeholder = 'ID' if view_settings['GET_BY'] == 'pk' else view_settings['GET_BY']
    user_id = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': placeholder}))
    login_by = view_settings['LOGIN_BY']
    login_button = view_settings['LOGIN_BUTTON']
    print(login_button)

    def __init__(self, *args, **kwargs):
        super(EasyLoginForm, self).__init__(*args, **kwargs)
        if args:
            self.fields['user_name'].queryset = User.objects.filter(**view_settings['FILTER'])
        else:
            self.fields['user_name'].queryset = User.objects.filter(**view_settings['FILTER'])[:view_settings['LIMIT']]

    def clean(self):
        """
        Validation if one from two params present in request.
        :return:
        """
        cleaned_data = super(EasyLoginForm, self).clean()
        user_name = cleaned_data.get("user_name")
        user_id = cleaned_data.get("user_id")

        if not any([user_name, user_id]):  # pragma: no cover
            raise forms.ValidationError("Please provide parameter user_name or user_id.")
