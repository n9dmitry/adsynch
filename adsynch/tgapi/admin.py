from django.contrib import admin
from .models import Car, Job, Realty


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['car_brand', 'car_model', 'car_year', 'car_price', 'seller_name']
    search_fields = ['car_brand', 'car_model', 'seller_name']
    list_filter = ['car_brand', 'car_year', 'seller_name']

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('new_id', 'job_title')
    list_filter = ('job_title',)
    search_fields = ('job_title', 'job_requirements')

@admin.register(Realty)
class RealtyAdmin(admin.ModelAdmin):
    list_display = ('new_id', 'realty_deal', 'realty_type', 'realty_square')
    list_filter = ('realty_type', 'realty_deal')
    search_fields = ('realty_type', 'realty_deal')