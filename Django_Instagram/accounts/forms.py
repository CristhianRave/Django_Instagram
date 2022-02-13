
from django import forms
from django.core import validators

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

    password1 = forms.CharField(label = 'Enter password', 
                                widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirm password', 
                                widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 
                  'last_name', 'email', 'password1', 'password2']

        help_texts = {
            'username': None, 
            'password1': None, 
            'password2': None, 
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
