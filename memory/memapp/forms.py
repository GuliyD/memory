from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Person


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, required=True)

    class Meta:
        model = Person
        fields = ['email', 'username', 'password1', 'password2']


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=60, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class CreateTaskForm(forms.Form):
    theme = forms.CharField(max_length=120, required=True)
    text = forms.CharField(widget=forms.Textarea, required=True)