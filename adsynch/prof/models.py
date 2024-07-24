from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Поле, связанное с моделью User
    telegram_login = models.CharField(max_length=50, blank=True, null=True, default='default_telegram_login')
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Предполагается использование формата для номеров телефонов
    name = models.CharField(max_length=100, default='John Doe')
    city = models.CharField(max_length=100, default='New York')
    email = models.EmailField(default='xyi')

    def __str__(self):
        return self.user.username + "'s Profile"
