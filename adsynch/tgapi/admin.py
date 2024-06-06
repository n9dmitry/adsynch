from django.contrib import admin
from .models import CarAd, JobAd, RealtyAd





@admin.register(CarAd)
class CarAdAdmin(admin.ModelAdmin):
    list_display = ['car_brand', 'car_model', 'car_year', 'car_price']
    search_fields = ['car_brand', 'car_model']
    list_filter = ['car_brand', 'car_year']

@admin.register(JobAd)
class JobAdAdmin(admin.ModelAdmin):
    list_display = ('title', 'ad_id')
    list_filter = ('title',)
    search_fields = ('title', 'job_requirements')

@admin.register(RealtyAd)
class RealtyAdAdmin(admin.ModelAdmin):
    list_display = ('ad_id', 'realty_deal', 'realty_type', 'realty_square')
    list_filter = ('realty_type', 'realty_deal')
    search_fields = ('realty_type', 'realty_deal')