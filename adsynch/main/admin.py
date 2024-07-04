from django.contrib import admin
from .models import AboutPage, ServicesPage, Bnr, SliderImage

class BnrAdmin(admin.ModelAdmin):
    list_display = ('position',)

admin.site.register(Bnr, BnrAdmin)


class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Опционально: поля, которые вы хотите отображать в списке объектов в админке

admin.site.register(AboutPage, AboutPageAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Поля, которые будут отображаться в списке услуг

admin.site.register(ServicesPage, ServiceAdmin)


class SliderImageAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Определяем какие поля отображать в списке объектов
    search_fields = ('title',)  # Добавляем поиск по указанным полям

admin.site.register(SliderImage, SliderImageAdmin)