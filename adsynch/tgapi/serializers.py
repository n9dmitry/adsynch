from rest_framework import serializers
from .models import CarAd, RealtyAd, JobAd

class CarAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAd
        fields = '__all__'

class RealtyAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealtyAd
        fields = '__all__'

class JobAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobAd
        fields = '__all__'