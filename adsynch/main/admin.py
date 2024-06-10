from django.contrib import admin
from .models import AboutPage
#
# class BannerAdmin(admin.ModelAdmin):
#     list_display = ['name', 'image']
#
# admin.site.register(Banner, BannerAdmin)


class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Опционально: поля, которые вы хотите отображать в списке объектов в админке

admin.site.register(AboutPage, AboutPageAdmin)