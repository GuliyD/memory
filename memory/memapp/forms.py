from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Person


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, required=True)

    class Meta:
        model = Person
        fields = ['email', 'username', 'password1', 'password2']
