from rest_framework import serializers
from .models import CarAd, RealtyAd, JobAd


def save_image_from_url(image_url, category):
    import os
    import requests
    from django.core.files.base import ContentFile
    from django.core.files.storage import default_storage
    from urllib.parse import urlparse

    file_name = os.path.basename(urlparse(image_url).path)
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
        # fields = кастомные
    def create(self, validated_data):
        photos_urls = validated_data.pop('photos', None)
        if photos_urls:
            urls = [url.strip() for url in photos_urls.split(',') if url.strip()]
            if urls:
                saved_photos = [save_image_from_url(url, 'car') for url in urls if save_image_from_url(url, 'car')]
                validated_data['photos'] = ','.join(saved_photos)
        return super().create(validated_data)

class RealtyAdSerializer(serializers.ModelSerializer):


    realty_type = serializers.CharField(allow_null=True, required=False)
    realty_commercial_type = serializers.CharField(allow_null=True, required=False)
    realty_rooms = serializers.IntegerField(allow_null=True, required=False)
    realty_floors_total = serializers.IntegerField(allow_null=True, required=False)
    realty_floor = serializers.IntegerField(allow_null=True, required=False)

    class Meta:
        model = RealtyAd
        fields = '__all__'
    def create(self, validated_data):
        user = validated_data.pop('user', None)
        instance = self.Meta.model(**validated_data)
        if user is not None:
            instance.user = user
        instance.save()
        return instance

class JobAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobAd
        fields = '__all__'