from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # Добавьте здесь необходимые поля для хранения данных

    def __str__(self):
        return self.name

class Banner(models.Model):
    name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='static/media')