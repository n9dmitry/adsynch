import django_filters
from .models import CarAd, RealtyAd, JobAd


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
        fields = ['price_min', 'price_max', 'year_min', 'year_max', 'mileage_min', 'mileage_max', 'brand', 'model',
                  'condition']


# Пытаюсь сделать остальные категории
class RealtyAdFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="car_price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="car_price", lookup_expr='lte')
    realty_deal = django_filters.CharFilter(field_name="realty_deal")
    realty_type = django_filters.CharFilter(field_name="realty_type")
    realty_commercial_type = django_filters.CharFilter(field_name="realty_commercial_type")
    realty_square_min = django_filters.NumberFilter(field_name="realty_square", lookup_expr='gte')
    realty_square_max = django_filters.NumberFilter(field_name="realty_square", lookup_expr='lte')
    realty_rooms_min = django_filters.NumberFilter(field_name="realty_rooms", lookup_expr='gte')
    realty_rooms_max = django_filters.NumberFilter(field_name="realty_rooms", lookup_expr='lte')

    class Meta:
        model = RealtyAd
        fields = ['price_min', 'price_max', 'realty_deal', 'realty_type', 'realty_commercial_type', 'realty_square_min', 'realty_square_max',
                  'realty_rooms_min', 'realty_rooms_max']


class JobAdFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="car_price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="car_price", lookup_expr='lte')
    job_category = django_filters.CharFilter(field_name="job_category")

    class Meta:
        model = JobAd
        fields = ['price_min', 'price_max', 'job_category']
