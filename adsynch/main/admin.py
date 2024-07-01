from django.contrib import admin
from .models import AboutPage, ServicesPage, Bnr

class BnrAdmin(admin.ModelAdmin):
    list_display = ('position',)

admin.site.register(Bnr, BnrAdmin)


class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Опционально: поля, которые вы хотите отображать в списке объектов в админке

admin.site.register(AboutPage, AboutPageAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Поля, которые будут отображаться в списке услуг

admin.site.register(ServicesPage, ServiceAdmin)