from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    grade = forms.IntegerField(required=True)
    section = forms.CharField(required=True)

    class Meta:
        model = User
        fields =[
            "username",
            "password1",
            "password2",
            "email",
            "grade",
            "section"

        ]
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }
    def save(self,commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        
        if commit:
            user.save()
            profile = Profile(user=user, grade = self.cleaned_data["grade"], section=self.cleaned_data["section"])
            profile.email = user.email
            profile.save()
        return user