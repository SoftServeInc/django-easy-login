from django import forms
from django.contrib.auth.models import User


class EasyLoginForm(forms.Form):
    user_name = forms.ModelChoiceField(queryset=User.objects.none(), required=False)
    user_id = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'ID'}))

    def __init__(self, *args, **kwargs):
        super(EasyLoginForm, self).__init__(*args, **kwargs)
        self.fields['user_name'].queryset = User.objects.all()

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
