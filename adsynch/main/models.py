from django.db import models


class Bnr(models.Model):
    POSITION_CHOICES = (
        ('top', 'Top'),
        ('center', 'Center'),
        ('bottom', 'Bottom'),
    )

    image = models.ImageField(upload_to='media/', blank=True)
    position = models.CharField(max_length=6, choices=POSITION_CHOICES)

    def __str__(self):
        return f"{self.get_position_display()} баннер"

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # Добавьте здесь необходимые поля для хранения данных

    def __str__(self):
        return self.name

class AboutPage(models.Model):
    image = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=200, default="О нас")
    description = models.TextField()

    def __str__(self):
        return self.title

class ServicesPage(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название услуги')
    description = models.TextField(verbose_name='Описание услуги')

    def __str__(self):
        return self.title

class SliderImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slider_images/')
    caption = models.TextField(blank=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title