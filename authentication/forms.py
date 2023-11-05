from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields =[
            "username",
            "password1",
            "password2",
            "email"
        ]
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }
