import django_filters
from .models import CarAd, RealtyAd, JobAd


# основной фильтр сортировки
class BaseFilterSet(django_filters.FilterSet):
    order_by = django_filters.OrderingFilter(
        fields=(
            ('date_published', '-date_published'),
            ('views', '-views'),
            ('price', '-car_price'),
        ),
        field_labels={
            'date_published': 'Новинки',
            'views': 'Просмотры',
            'price': 'Цена',
        },
        label='Сортировка',
        choices=(
            ('date_published', 'Новинки'),
            ('-date_published', 'Новинки (по убыванию)'),
            ('views', 'Просмотры (минимум)'),
            ('-views', 'Просмотры (максимум)'),
            ('price', 'Цена (дешевые)'),
            ('-price', 'Цена (дорогие)'),
        )
    )
class CarAdFilter(BaseFilterSet, django_filters.FilterSet, ):
    price_min = django_filters.NumberFilter(field_name="car_price", label="Цена Min", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="car_price", label="Цена Max", lookup_expr='lte')
    brand = django_filters.ChoiceFilter(
        field_name="car_brand",
        label="Бренд",
        choices=[(brand, brand) for brand in CarAd.objects.values_list('car_brand', flat=True).distinct()]
    )
    model = django_filters.ChoiceFilter(
        field_name="car_model",
        label="Модель",
        choices=[(car_model, car_model) for car_model in CarAd.objects.values_list('car_model', flat=True).distinct()]
    )

    condition = django_filters.ChoiceFilter(
        field_name="car_condition",
        label="Состояние",
        choices=[(car_condition, car_condition) for car_condition in
                 CarAd.objects.values_list('car_condition', flat=True).distinct()]
    )
    year_min = django_filters.NumberFilter(field_name="car_year", label="Год Min", lookup_expr='gte')
    year_max = django_filters.NumberFilter(field_name="car_year", label="Год Max", lookup_expr='lte')
    mileage_min = django_filters.NumberFilter(field_name="car_mileage", label="Пробег Min", lookup_expr='gte')
    mileage_max = django_filters.NumberFilter(field_name="car_mileage", label="Пробег Min", lookup_expr='lte')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.fields['model'].disabled = True

    class Meta:
        model = CarAd
        fields = ['order_by', 'price_min', 'price_max', 'brand', 'model',
                  'condition', 'year_min', 'year_max', 'mileage_min', 'mileage_max', ]


# Пытаюсь сделать остальные категории
class RealtyAdFilter(BaseFilterSet, django_filters.FilterSet):
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
    realty_square_min = django_filters.NumberFilter(field_name="realty_square", label="Площадь Min", lookup_expr='gte')
    realty_square_max = django_filters.NumberFilter(field_name="realty_square", label="Площадь Max", lookup_expr='lte')
    realty_rooms_min = django_filters.NumberFilter(field_name="realty_rooms", label="Комнат Max", lookup_expr='gte')
    realty_rooms_max = django_filters.NumberFilter(field_name="realty_rooms", label="Комнат Max", lookup_expr='lte')

    class Meta:
        model = RealtyAd
        fields = ['order_by', 'price_min', 'price_max', 'realty_deal', 'realty_type', 'realty_commercial_type', 'realty_square_min',
                  'realty_square_max',
                  'realty_rooms_min', 'realty_rooms_max']



class JobAdFilter(BaseFilterSet, django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="price", label="Зарплата от", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="price", label="Зарплата до", lookup_expr='lte')
    job_category = django_filters.ChoiceFilter(
        field_name="job_category",
        label="Категория",
        choices=JobAd.objects.order_by().values_list('job_category', 'job_category').distinct()
    )

    class Meta:
        model = JobAd
        fields = ['order_by', 'price_min', 'price_max', 'job_category']
