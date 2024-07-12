from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import CarAd, JobAd, RealtyAd, UserProfileLink
from .serializers import CarAdSerializer, JobAdSerializer, RealtyAdSerializer
import os
from django.shortcuts import render
import json
from django.core.exceptions import ValidationError
from django.views.generic import DetailView
import logging
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django_filters.views import FilterView
from .filters import CarAdFilter, RealtyAdFilter, JobAdFilter

logger = logging.getLogger(__name__)

from django.http import JsonResponse
from adsynch.tasks import get_usd_rate



def get_currency_rate(request):
    rate = get_usd_rate()
    print(rate)
    return JsonResponse({'rate': rate})


class CarAdListView(FilterView):
    model = CarAd
    template_name = 'tgapi/cars.html'  # Убедитесь, что путь правильный
    context_object_name = 'car_ads'
    filterset_class = CarAdFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        order_by = self.request.GET.get('order_by')
        if order_by:
            queryset = queryset.order_by(order_by)
        return queryset


def get_models(request):
    brand = request.GET.get('brand')
    models = CarAd.objects.filter(car_brand=brand).values_list('car_model', flat=True).distinct()
    return JsonResponse({'models': list(models)})
class RealtyAdListView(FilterView):
    model = RealtyAd
    template_name = 'tgapi/realty.html'  # Убедитесь, что путь правильный
    context_object_name = 'realty_ads'
    filterset_class = RealtyAdFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        order_by = self.request.GET.get('order_by')
        if order_by:
            queryset = queryset.order_by(order_by)
        return queryset

class JobAdListView(FilterView):
    model = JobAd
    template_name = 'tgapi/jobs.html'  # Убедитесь, что путь правильный
    context_object_name = 'job_ads'
    filterset_class = JobAdFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        order_by = self.request.GET.get('order_by')
        if order_by:
            queryset = queryset.order_by(order_by)
        return queryset

@require_http_methods(["GET"])
@api_view(['GET'])
def my_ads(request, username):
    if not username:
        return Response({'error': 'Username not provided'}, status=status.HTTP_400_BAD_REQUEST)

    user = get_object_or_404(User, username=username)

    car_ads = CarAd.objects.filter(user=user)
    realty_ads = RealtyAd.objects.filter(user=user)
    job_ads = JobAd.objects.filter(user=user)

    car_ads_serializer = CarAdSerializer(car_ads, many=True)
    realty_ads_serializer = RealtyAdSerializer(realty_ads, many=True)
    job_ads_serializer = JobAdSerializer(job_ads, many=True)

    ads_data = {
        'car_ads': car_ads_serializer.data,
        'realty_ads': realty_ads_serializer.data,
        'job_ads': job_ads_serializer.data
    }

    return Response(ads_data, status=status.HTTP_200_OK)


@csrf_exempt
@require_http_methods(["POST"])
def generate_link(request):
    data = json.loads(request.body)
    username = data.get('username')

    token = get_random_string(length=32)
    user_profile_link = UserProfileLink(username=username, token=token)
    user_profile_link.save()

    link = f"http://127.0.0.1:8000/api/{username}/{token}/"
    return JsonResponse({'link': link})


def profile_view(request, username, token):
    user_profile_link = get_object_or_404(UserProfileLink, username=username, token=token)
    user = get_object_or_404(User, username=user_profile_link.username)
    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    user_profile_link.delete()
    return redirect('/')


# @csrf_exempt
# @require_http_methods(["GET"])
# def check_user(request, username):
#     exists = User.objects.filter(username=username).exists()
#     print(JsonResponse({'exists': exists}))
#     return JsonResponse({'exists': exists})

@csrf_exempt
@require_http_methods(["GET"])
def check_user(request, username):
    print("Received request for username:", username)
    exists = User.objects.filter(username=username).exists()
    print("User exists:", exists)  # Отладочный вывод результата запроса к базе данных
    return JsonResponse({'exists': exists})

def get_or_create_user(data):
    user_id = data['user_id']
    username = f"user_{user_id}"
    hex_password = get_random_string(length=32)

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        user = User.objects.create_user(username=username, password=hex_password)

    return user


class CarAdView(APIView):
    def post(self, request):
        print("Received data:", request.data)
        user = get_or_create_user(request.data)
        dt = request.data.copy()
        dt['user'] = user.id
        dt['is_active'] = 'True'

        serializer = CarAdSerializer(data=dt)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RealtyAdView(APIView):
    def post(self, request, *args, **kwargs):
        logger.debug("Received data: %s", request.data)
        user = get_or_create_user(request.data)

        dt = request.data.copy()
        for key, value in dt.items():
            if isinstance(value, str) and value.lower() == 'none':
                dt[key] = None

        dt['user'] = user.id
        dt['is_active'] = 'True'

        serializer = RealtyAdSerializer(data=dt)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobAdView(APIView):
    def post(self, request):
        print("Received data:", request.data)
        user = get_or_create_user(request.data)
        dt = request.data.copy()

        dt['user'] = user.id
        dt['is_active'] = 'True'

        serializer = JobAdSerializer(data=dt)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewCountMixin:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        self.model.objects.filter(pk=obj.pk).update(views=F('views') + 1)
        obj.refresh_from_db()
        return obj

class CarAdDetailView(ViewCountMixin, DetailView):
    model = CarAd
    template_name = 'tgapi/car_detail.html'
    context_object_name = 'car_ad'

class JobAdDetailView(ViewCountMixin, DetailView):
    model = JobAd
    template_name = 'tgapi/jobs_detail.html'
    context_object_name = 'job_ad'

class RealtyAdDetailView(ViewCountMixin, DetailView):
    model = RealtyAd  # Указываем модель, по которой будет строиться DetailView
    template_name = 'tgapi/realty_detail.html'  # Указываем шаблон для отображения детальной информации
    context_object_name = 'realty_ad'  # Имя контекстного объекта для доступа к данным в шаблоне


# def cars(request):
#     car_ads = CarAd.objects.all()
#     # Получение уникальных марок авто и передача их в шаблон
#     car_brands = CarAd.objects.values_list('car_brand', flat=True).distinct()
#
#     selected_brand = request.GET.get('car_brand')
#     selected_model = request.GET.get('car_model')
#     price_from = request.GET.get('price_from')
#     price_to = request.GET.get('price_to')
#
#     # Если выбрана марка, фильтровать по выбранной марке и ее моделям
#     if selected_brand:
#         car_ads = car_ads.filter(car_brand=selected_brand)
#         # Получение уникальных моделей для выбранной марки
#         car_models = CarAd.objects.filter(car_brand=selected_brand).values_list('car_model', flat=True).distinct()
#     else:
#         car_models = []
#
#     # Фильтрация по диапазону цен
#     if price_from:
#         car_ads = car_ads.filter(price__gte=price_from)
#     if price_to:
#         car_ads = car_ads.filter(price__lte=price_to)
#
#     return render(request, 'tgapi/cars.html', {
#         'car_ads': car_ads,
#         'car_brands': car_brands,
#         'selected_brand': selected_brand,
#         'car_models': car_models,
#         'selected_model': selected_model,
#         'price_from': price_from,
#         'price_to': price_to
#     })
#
# def jobs(request):
#     selected_category = request.GET.get('category', None)
#     min_price = request.GET.get('min_price')
#     max_price = request.GET.get('max_price')
#
#     job_ads = JobAd.objects.filter(is_active=True)
#
#     categories = JobAd.objects.values_list('category', flat=True).distinct()
#
#     if selected_category:
#         job_ads = job_ads.filter(category=selected_category)
#
#     if min_price is not None:
#         job_ads = job_ads.filter(price__gte=min_price)
#
#     if max_price is not None:
#         job_ads = job_ads.filter(price__lte=max_price)
#
#     return render(request, 'tgapi/jobs.html', {'job_ads': job_ads, 'categories': categories})
#
# def realtys(request):
#     selected_realty_type = request.GET.get('realty_type', None)
#     selected_realty_deal = request.GET.get('realty_deal', None)
#     sort_by = request.GET.get('sort_by', None)
#
#     realty_ads = RealtyAd.objects.all()
#
#     realty_types = RealtyAd.objects.values_list('realty_type', flat=True).distinct()
#     realty_deals = RealtyAd.objects.values_list('realty_deal', flat=True).distinct()
#
#     if selected_realty_type:
#         realty_ads = realty_ads.filter(realty_type=selected_realty_type)
#
#     if selected_realty_deal:
#         realty_ads = realty_ads.filter(realty_deal=selected_realty_deal)
#
#     if sort_by == 'date_published':
#         realty_ads = realty_ads.order_by('-date_published')
#     elif sort_by == '-date_published':
#         realty_ads = realty_ads.order_by('date_published')
#
#     return render(request, 'tgapi/realty.html',
#                   {'realty_ads': realty_ads, 'realty_types': realty_types, 'realty_deals': realty_deals})

