import django_filters
from .models import CarAd

class CarAdFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="car_price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="car_price", lookup_expr='lte')
    year_min = django_filters.NumberFilter(field_name="car_year", lookup_expr='gte')
    year_max = django_filters.NumberFilter(field_name="car_year", lookup_expr='lte')
    mileage_min = django_filters.NumberFilter(field_name="car_mileage", lookup_expr='gte')
    mileage_max = django_filters.NumberFilter(field_name="car_mileage", lookup_expr='lte')
    brand = django_filters.CharFilter(field_name="car_brand", lookup_expr='icontains')
    model = django_filters.CharFilter(field_name="car_model", lookup_expr='icontains')
    condition = django_filters.CharFilter(field_name="car_condition", lookup_expr='icontains')

    class Meta:
        model = CarAd
        fields = ['price_min', 'price_max', 'year_min', 'year_max', 'mileage_min', 'mileage_max', 'brand', 'model', 'condition']