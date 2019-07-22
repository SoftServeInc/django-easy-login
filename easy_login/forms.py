from django import forms
from django.contrib.auth.models import User


class SwitchUserForm(forms. Form):
    user = forms.ModelChoiceField(queryset=User.objects.none())

    def __init__(self, *args, **kwargs):
        super(SwitchUserForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.all()
