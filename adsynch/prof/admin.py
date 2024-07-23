from django.contrib import admin
from .models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)  # Опционально: поля, которые вы хотите отображать в списке объектов в админке

admin.site.register(UserProfile, UserProfileAdmin)