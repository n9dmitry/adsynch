from rest_framework import serializers
from .models import CarAd, RealtyAd, JobAd
import os
import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from urllib.parse import urlparse
from datetime import datetime


def save_image_from_url(image_url, category, ad_id, photo_number):
    # Формируем имя файла в формате "дата(ГГММДД)_id_номер фото"
    now = datetime.now().strftime("%y%m%d")
    file_extension = os.path.splitext(urlparse(image_url).path)[1]
    file_name = f"{now}_{ad_id}_{photo_number}{file_extension}"
    file_path = os.path.join('ads_img', category, file_name)

    response = requests.get(image_url)
    if response.status_code == 200:
        file_content = ContentFile(response.content)
        full_path = default_storage.save(file_path, file_content)
        return full_path
    return None


class CarAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAd
        fields = '__all__'

    def create(self, validated_data):
        photos_urls = validated_data.pop('photos', None)
        car_ad = super().create(validated_data)  # Создаем объявление и получаем его экземпляр
        if photos_urls:
            urls = [url.strip() for url in photos_urls.split(',') if url.strip()]
            if urls:
                saved_photos = []
                ad_id = car_ad.id  # Используем ID созданного объявления
                for idx, url in enumerate(urls):
                    saved_photo = save_image_from_url(url, 'car', ad_id, idx + 1)
                    if saved_photo:
                        saved_photos.append(saved_photo)
                car_ad.photos = ','.join(saved_photos)
                car_ad.save()  # Сохраняем обновленное объявление с путями к фотографиям
        return car_ad

class RealtyAdSerializer(serializers.ModelSerializer):


    realty_type = serializers.CharField(allow_null=True, required=False)
    realty_commercial_type = serializers.CharField(allow_null=True, required=False)
    realty_rooms = serializers.IntegerField(allow_null=True, required=False)
    realty_floors_total = serializers.IntegerField(allow_null=True, required=False)
    realty_floor = serializers.IntegerField(allow_null=True, required=False)

    class Meta:
        model = RealtyAd
        fields = '__all__'
    # def create(self, validated_data):
    #     user = validated_data.pop('user', None)
    #     instance = self.Meta.model(**validated_data)
    #     if user is not None:
    #         instance.user = user
    #     instance.save()
    #     return instance

class JobAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobAd
        fields = '__all__'