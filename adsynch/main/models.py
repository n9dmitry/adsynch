from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # Добавьте здесь необходимые поля для хранения данных

    def __str__(self):
        return self.name

# class Banner(models.Model):
#     name = models.CharField(max_length=100, blank=True)
#     image = models.ImageField(upload_to='static/media')

class AboutPage(models.Model):
    image = models.ImageField(upload_to='about_images/')
    title = models.CharField(max_length=200, default="О нас")
    description = models.TextField()

    def __str__(self):
        return self.title

class ServicesPage(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название услуги')
    description = models.TextField(verbose_name='Описание услуги')

    def __str__(self):
        return self.title
