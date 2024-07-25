from rest_framework import serializers
from .models import CarAd, RealtyAd, JobAd, UserProfile
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

class AdBaseSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        photos_urls = validated_data.pop('photos', None)
        ad_instance = super().create(validated_data)
        if photos_urls:
            urls = [url.strip() for url in photos_urls.split(',') if url.strip()]
            if urls:
                saved_photos = []
                ad_id = ad_instance.id  # Используем ID созданного объявления
                for idx, url in enumerate(urls):
                    saved_photo = save_image_from_url(url, self.Meta.model._meta.model_name, ad_id, idx + 1)
                    if saved_photo:
                        saved_photos.append(saved_photo)
                ad_instance.photos = ','.join(saved_photos)
                ad_instance.save()  # Сохраняем обновленное объявление с путями к фотографиям
        return ad_instance

class CarAdSerializer(AdBaseSerializer):
    class Meta:
        model = CarAd
        fields = '__all__'

class RealtyAdSerializer(AdBaseSerializer):
    realty_type = serializers.CharField(allow_null=True, required=False)
    realty_commercial_type = serializers.CharField(allow_null=True, required=False)
    realty_rooms = serializers.IntegerField(allow_null=True, required=False)
    realty_floors_total = serializers.IntegerField(allow_null=True, required=False)
    realty_floor = serializers.IntegerField(allow_null=True, required=False)

    class Meta:
        model = RealtyAd
        fields = '__all__'

class JobAdSerializer(AdBaseSerializer):
    class Meta:
        model = JobAd
        fields = '__all__'


