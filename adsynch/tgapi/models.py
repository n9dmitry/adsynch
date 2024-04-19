from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Car(models.Model):
    user_id = models.IntegerField(default=2)  # поле для хранения ID пользователя
    new_id = models.IntegerField()
    car_brand = models.CharField(max_length=255)
    car_model = models.CharField(max_length=255)
    car_year = models.IntegerField()
    car_body_type = models.CharField(max_length=255)
    car_engine_type = models.CharField(max_length=255)
    car_engine_volume = models.CharField(max_length=255)
    car_power = models.CharField(max_length=255)
    car_transmission_type = models.CharField(max_length=255)
    car_color = models.CharField(max_length=255)
    car_mileage = models.TextField()
    car_document_status = models.CharField(max_length=255)
    car_owners = models.TextField()
    car_customs_cleared = models.TextField()
    car_condition = models.CharField(max_length=255)
    car_description = models.TextField()
    currency = models.CharField(max_length=255)
    car_price = models.FloatField()
    car_location = models.CharField(max_length=255)
    seller_name = models.CharField(max_length=255)
    seller_phone = models.CharField(max_length=20)
    photos = models.TextField(blank=True)
    date_published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.car_brand + " " + self.car_model
    def save(self, *args, **kwargs):
        if not self.user_id:  # Если user_id не указан
            user = User.objects.create_user(username=f"user_{self.id}")
            self.user_id = user.id
        else:  # Если пользователь существует
            try:
                user = User.objects.get(id=self.user_id)
            except User.DoesNotExist:
                user = User.objects.create_user(username=f"user_{self.user_id}")
        super(Car, self).save(*args, **kwargs)

class Job(models.Model):
    user_id = models.IntegerField(default=2)
    new_id = models.CharField(max_length=100)
    job_title = models.CharField(max_length=255)
    job_requirements = models.TextField()
    job_responsibilities = models.TextField()
    job_conditions = models.TextField()
    job_contacts = models.CharField(max_length=255)
    photos = models.TextField()


    def __str__(self):
        return self.job_title

    def save(self, *args, **kwargs):
        if not self.user_id:  # Если user_id не указан
            user = User.objects.create_user(username=f"user_{self.id}")
            self.user_id = user.id
        else:  # Если пользователь существует
            try:
                user = User.objects.get(id=self.user_id)
            except User.DoesNotExist:
                user = User.objects.create_user(username=f"user_{self.user_id}")
        super(Job, self).save(*args, **kwargs)

class Realty(models.Model):
    user_id = models.IntegerField(default=2)
    new_id = models.CharField(max_length=100)
    realty_deal = models.CharField(max_length=100)
    realty_type = models.CharField(max_length=100)
    realty_square = models.FloatField()
    photos = models.TextField()

    def __str__(self):
        return f"{self.realty_type} - {self.realty_deal}"

    def save(self, *args, **kwargs):
        if not self.user_id:  # Если user_id не указан
            user = User.objects.create_user(username=f"user_{self.user_id}")
            self.user_id = user.id
        else:  # Если пользователь существует
            try:
                user = User.objects.get(id=self.user_id)
            except User.DoesNotExist:
                user = User.objects.create_user(username=f"user_{self.user_id}")
        super(Realty, self).save(*args, **kwargs)

