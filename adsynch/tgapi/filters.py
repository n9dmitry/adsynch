import django_filters
from .models import CarAd, RealtyAd, JobAd


class CarAdFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="car_price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="car_price", lookup_expr='lte')
    year_min = django_filters.NumberFilter(field_name="car_year", lookup_expr='gte')
    year_max = django_filters.NumberFilter(field_name="car_year", lookup_expr='lte')
    mileage_min = django_filters.NumberFilter(field_name="car_mileage", lookup_expr='gte')
    mileage_max = django_filters.NumberFilter(field_name="car_mileage", lookup_expr='lte')
    brand = django_filters.ChoiceFilter(
        field_name="car_brand",
        choices=[(brand, brand) for brand in CarAd.objects.values_list('car_brand', flat=True).distinct()]
    )
    model = django_filters.ChoiceFilter(
        field_name="car_model",
        choices=[(car_model, car_model) for car_model in CarAd.objects.values_list('car_model', flat=True).distinct()]
    )

    condition = django_filters.ChoiceFilter(
        field_name="car_condition",
        choices=[(car_condition, car_condition) for car_condition in
                 CarAd.objects.values_list('car_condition', flat=True).distinct()]
    )

    class Meta:
        model = CarAd
        fields = ['price_min', 'price_max', 'year_min', 'year_max', 'mileage_min', 'mileage_max', 'brand', 'model',
                  'condition']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'brand' in self.data and self.data['brand']:
            brand = self.data['brand']
            self.filters['model'].extra.update({
                'choices': [(model, model) for model in
                            CarAd.objects.filter(car_brand=brand).values_list('car_model', flat=True).distinct()]
            })


# Пытаюсь сделать остальные категории
class RealtyAdFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="price", label="Цена Min", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="price", label="Цена Max", lookup_expr='lte')
    realty_deal = django_filters.ChoiceFilter(
        field_name="realty_deal",
        label="Тип сделки",
        choices=[(realty_deal, realty_deal) for realty_deal in
                 RealtyAd.objects.values_list('realty_deal', flat=True).distinct()]
    )
    realty_type = django_filters.ChoiceFilter(
        field_name="realty_type",
        label="Тип недвижимости",
        choices=[(realty_type, realty_type) for realty_type in
                 RealtyAd.objects.values_list('realty_type', flat=True).distinct()]
    )
    realty_commercial_type = django_filters.ChoiceFilter(
        field_name="realty_commercial_type",
        label="Тип коммерческой недвижимости",
        choices=[(realty_commercial_type, realty_commercial_type) for realty_commercial_type in
                 RealtyAd.objects.values_list('realty_commercial_type', flat=True).distinct()]
    )
    # realty_deal = django_filters.CharFilter(field_name="realty_deal")
    # realty_type = django_filters.CharFilter(field_name="realty_type")
    # realty_commercial_type = django_filters.CharFilter(field_name="realty_commercial_type")
    realty_square_min = django_filters.NumberFilter(field_name="realty_square", label="Площадь Min", lookup_expr='gte')
    realty_square_max = django_filters.NumberFilter(field_name="realty_square", label="Площадь Max", lookup_expr='lte')
    realty_rooms_min = django_filters.NumberFilter(field_name="realty_rooms", label="Комнат Max", lookup_expr='gte')
    realty_rooms_max = django_filters.NumberFilter(field_name="realty_rooms", label="Комнат Max", lookup_expr='lte')

    class Meta:
        model = RealtyAd
        fields = ['price_min', 'price_max', 'realty_deal', 'realty_type', 'realty_commercial_type', 'realty_square_min',
                  'realty_square_max',
                  'realty_rooms_min', 'realty_rooms_max']

    #     Тут надо будет переделать если коммерческий тип недвижимости
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if 'brand' in self.data and self.data['brand']:
    #         brand = self.data['brand']
    #         self.filters['model'].extra.update({
    #             'choices': [(model, model) for model in
    #                         CarAd.objects.filter(car_brand=brand).values_list('car_model', flat=True).distinct()]
    #         })


class JobAdFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="price", label="Зарплата от", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="price", label="Зарплата до", lookup_expr='lte')
    job_category = django_filters.ChoiceFilter(
        field_name="job_category",
        label="Категория",
        choices=JobAd.objects.order_by().values_list('job_category', 'job_category').distinct()
    )

    class Meta:
        model = JobAd
        fields = ['price_min', 'price_max', 'job_category']
