from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
    UsernameField,
)

from users.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
        ]
        field_classes = {"username": UsernameField}


class UpdateMyProfileForm(UserChangeForm):
    username = UsernameField(disabled=True)
    email = forms.EmailField(disabled=True)
    password = None

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
        ]


class LoginForm(AuthenticationForm):
    pass

