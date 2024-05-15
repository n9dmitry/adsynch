from rest_framework import serializers
from .models import CarAd, RealtyAd, JobAd



class CarAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAd
        fields = '__all__'

class RealtyAdSerializer(serializers.ModelSerializer):


    realty_type = serializers.CharField(allow_null=True, required=False)
    realty_commercial_type = serializers.CharField(allow_null=True, required=False)
    realty_rooms = serializers.IntegerField(allow_null=True, required=False)
    realty_floors_total = serializers.IntegerField(allow_null=True, required=False)
    realty_floor = serializers.IntegerField(allow_null=True, required=False)

    class Meta:
        model = RealtyAd
        fields = '__all__'


class JobAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobAd
        fields = '__all__'