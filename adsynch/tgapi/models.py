from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class UserProfileLink(models.Model):
    username = models.CharField(max_length=255)
    token = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.token}"

def validate_integer(value):
    try:
        int(value)
    except (TypeError, ValueError):
        raise ValidationError('Value must be an integer')

class Ads(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    username_tg = models.CharField(max_length=100, blank=True, null=True)
    ad_id = models.CharField(max_length=100, blank=True, null=True)
    photos = models.TextField(blank=True, null=True)
    date_published = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    contact_name = models.CharField(max_length=255, blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    currency = models.CharField(max_length=5, blank=True, null=True)
    price = models.CharField(max_length=25, blank=True, null=True, validators=[RegexValidator(regex='^\d+$', message='Price must be an integer')])
    description = models.TextField(max_length=400, blank=True, null=True)
    category = models.CharField(max_length=15, blank=True, null=True)
    views = models.PositiveIntegerField(default=0)  # Поле для счётчика просмотров

    class Meta:
        abstract = True


class CarAd(Ads):
    car_brand = models.CharField(max_length=255, blank=True, null=True)
    car_model = models.CharField(max_length=255, blank=True, null=True)
    car_year = models.IntegerField()
    car_body_type = models.CharField(max_length=255, blank=True, null=True)
    car_engine_type = models.CharField(max_length=255, blank=True, null=True)
    car_engine_volume = models.CharField(max_length=255, blank=True, null=True)
    car_power = models.CharField(max_length=255, blank=True, null=True)
    car_transmission_type = models.CharField(max_length=255, blank=True, null=True)
    car_color = models.CharField(max_length=255, blank=True, null=True)
    car_mileage = models.TextField(blank=True, null=True)
    car_document_status = models.CharField(max_length=255, blank=True, null=True)
    car_owners = models.TextField(blank=True, null=True)
    car_customs_cleared = models.TextField(blank=True, null=True)
    car_condition = models.CharField(max_length=255, blank=True, null=True)
    # car_description = models.TextField(blank=True, null=True)
    car_location = models.CharField(max_length=255, blank=True, null=True)
    car_name = models.CharField(max_length=255, blank=True, null=True)
    # car_phone = models.CharField(max_length=20, blank=True, null=True)


class RealtyAd(Ads):
    realty_deal = models.CharField(max_length=100, blank=True, null=True)
    realty_type = models.CharField(max_length=100, blank=True, null=True)
    realty_commercial_type = models.CharField(max_length=100, blank=True, null=True)
    realty_square = models.FloatField(blank=True, null=True)
    realty_location = models.CharField(max_length=255, blank=True, null=True)
    realty_rooms = models.IntegerField(blank=True, null=True)
    realty_floor = models.IntegerField(blank=True, null=True)
    realty_floors_total = models.IntegerField(blank=True, null=True)
    # realty_currency = models.CharField(max_length=255, blank=True, null=True)
    # realty_price = models.FloatField(blank=True, null=True)
    # realty_phone = models.CharField(max_length=255, blank=True, null=True)
    # realty_name = models.CharField(max_length=255, blank=True, null=True)


class JobAd(Ads):
    job_category = models.CharField(max_length=255, blank=True, null=True)
    # job_title = models.CharField(max_length=255, default='0')
    # job_description = models.TextField()
    # job_currency = models.CharField(max_length=255, default='0')
    # job_price = models.IntegerField(default='0')
    # job_contacts = models.CharField(max_length=255, default='0')
    # job_name = models.CharField(max_length=255, default='0')
