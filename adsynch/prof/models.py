from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username_tg = models.CharField(max_length=100, blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    contact_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username
