from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm


class RegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100, required=True, label='Имя')  # Добавляем поле name

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Email', max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email'}))
