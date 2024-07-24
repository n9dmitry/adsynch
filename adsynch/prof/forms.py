from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['telegram_login', 'phone_number', 'name', 'city', 'email']
        labels = {
            'telegram_login': 'Логин Telegram',
            'phone_number': 'Номер телефона',
            'name': 'Имя',
            'city': 'Город',
            'email': 'Email',
        }

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Введите номер телефона'
        self.fields['email'].widget.attrs['placeholder'] = 'example@example.com'
