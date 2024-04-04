from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100, required=True, label='Имя')  # Добавляем поле name

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
