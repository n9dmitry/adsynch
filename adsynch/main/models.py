from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # Добавьте здесь необходимые поля для хранения данных

    def __str__(self):
        return self.name