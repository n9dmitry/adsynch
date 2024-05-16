from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

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
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True

    # def set_info(self):
    #     pass
    #     if not self.user_id:  # Если user_id не указан
    #         user = User.objects.create_user(username=f"user_{self.id}")
    #         self.user = user
    #
    #     if isinstance(self, CarAd):
    #         self.contact_name = self.seller_name
    #         self.contact_phone = self.seller_phone
    #         self.title = f"{self.car_brand} {self.car_model} ({self.car_year})"
    #         self.currency = self.car_currency
    #         self.price = self.car_price
    #     elif isinstance(self, RealtyAd):
    #         self.contact_name = self.realty_name
    #         self.contact_phone = self.realty_contacts
    #         self.title = f"{self.rooms_number}-к. {self.realty_type}, {self.realty_square} м², {self.floor}/{self.total_floors} эт."
    #         self.currency = self.realty_currency
    #         self.price = self.realty_price
    #     elif isinstance(self, JobAd):
    #         self.contact_name = self.job_name
    #         self.contact_phone = self.job_contacts
    #         self.title = self.job_title
    #         self.currency = self.job_currency
    #         self.price = self.job_price
    #
    #     description_fields = [f"{field.name}: {getattr(self, field.name)}" for field in self._meta.get_fields() if
    #                           field.name not in ['id', 'user', 'date_published', 'is_active', 'contact_name',
    #                                              'contact_phone', 'description']]
    #     self.description = '\n'.join(description_fields)

    def save(self, *args, **kwargs):
        # self.set_info()
        super().save(*args, **kwargs)


class CarAd(Ads):
    car_brand = models.CharField(max_length=255, default='0')
    car_model = models.CharField(max_length=255, default='0')
    car_year = models.IntegerField()
    car_body_type = models.CharField(max_length=255, default='0')
    car_engine_type = models.CharField(max_length=255, default='0')
    car_engine_volume = models.CharField(max_length=255, default='0')
    car_power = models.CharField(max_length=255, default='0')
    car_transmission_type = models.CharField(max_length=255, default='0')
    car_color = models.CharField(max_length=255, default='0')
    car_mileage = models.TextField()
    car_document_status = models.CharField(max_length=255, default='0')
    car_owners = models.TextField()
    car_customs_cleared = models.TextField()
    car_condition = models.CharField(max_length=255, default='0')
    car_description = models.TextField()
    car_currency = models.CharField(max_length=255, default='0')
    car_price = models.FloatField(default='0')
    car_location = models.CharField(max_length=255, default='0')
    seller_name = models.CharField(max_length=255, default='0')
    seller_phone = models.CharField(max_length=20, default='0')


class RealtyAd(Ads):
    realty_deal = models.CharField(max_length=100, blank=True, null=True)
    realty_type = models.CharField(max_length=100, blank=True, null=True)
    realty_commercial_type = models.CharField(max_length=100, blank=True, null=True)
    realty_square = models.FloatField(blank=True, null=True)
    realty_location = models.CharField(max_length=255, blank=True, null=True)
    realty_rooms = models.IntegerField(blank=True, null=True)
    realty_floor = models.IntegerField(blank=True, null=True)
    realty_floors_total = models.IntegerField(blank=True, null=True)
    realty_currency = models.CharField(max_length=255, blank=True, null=True)
    realty_price = models.FloatField(blank=True, null=True)
    realty_contacts = models.CharField(max_length=255, blank=True, null=True)
    realty_name = models.CharField(max_length=255, blank=True, null=True)


class JobAd(Ads):
    job_title = models.CharField(max_length=255, default='0')
    job_description = models.TextField()
    job_currency = models.CharField(max_length=255, default='0')
    job_price = models.IntegerField(default='0')
    job_contacts = models.CharField(max_length=255, default='0')
    job_name = models.CharField(max_length=255, default='0')
