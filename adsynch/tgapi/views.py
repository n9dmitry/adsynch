from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import CarAd, JobAd, RealtyAd
from .serializers import CarAdSerializer, JobAdSerializer, RealtyAdSerializer
import os
from django.shortcuts import render
import json
from django.core.exceptions import ValidationError
from django.views.generic import DetailView
import logging
from django.contrib.auth.models import User


logger = logging.getLogger(__name__)


def get_or_create_user(data):
    user_id = data['user_id']
    username = f"user_{user_id}"
    hex_password = 100

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        user = User.objects.create_user(username=username, password=hex_password)

    return user


class CarAdView(APIView):
    def post(self, request):
        print("Received data:", request.data)
        user = get_or_create_user(request.data)

        serializer = CarAdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class RealtyAdView(APIView):
#     def post(self, request):
#         logger.debug("Received data:", request.data)  # Логируем данные запроса
#         serializer = RealtyAdSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         logger.error("Invalid data:", serializer.errors)  # Логируем ошибки валидации
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class RealtyAdView(APIView):
    def post(self, request, *args, **kwargs):
        logger.debug("Received data: %s", request.data)
        user = get_or_create_user(request.data)

        dt = request.data.copy()

        for key, value in dt.items():
            if isinstance(value, str) and value.lower() == 'none':
                dt[key] = None

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

        serializer = JobAdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)















# @csrf_exempt
# @require_POST
# def bot_webhook(request):
#     if request.method == 'POST':
#         data = request.POST
#
#         category = data.get('category')
#
#         if category is None:
#             return HttpResponse("Category is missing", status=400)
#
#         if category == 'car':
#             ad = CarAd(
#                 ad_id=data.get('ad_id'),
#                 car_brand=data.get('car_brand'),
#                 car_model=data.get('car_model'),
#                 car_year=data.get('car_year'),
#                 # car_body_type=data.get('car_body_type'),
#                 # car_engine_type=data.get('car_engine_type'),
#                 # car_engine_volume=data.get('car_engine_volume'),
#                 # car_power=data.get('car_power'),
#                 # car_transmission_type=data.get('car_transmission_type'),
#                 # car_color=data.get('car_color'),
#                 # car_mileage=data.get('car_mileage'),
#                 # car_document_status=data.get('car_document_status'),
#                 # car_owners=data.get('car_owners'),
#                 # car_customs_cleared=data.get('car_customs_cleared'),
#                 # car_condition=data.get('car_condition'),
#                 # car_description=data.get('car_description'),
#                 # car_currency=data.get('currency'),  # Передаем значение валюты
#                 # car_price=data.get('car_price'),  # Передаем цену
#                 # car_location=data.get('car_location'),
#                 # seller_name=data.get('seller_name'),
#                 # seller_phone=data.get('seller_phone'),
#                 # username=data.get('username'),
#                 # user_id=data.get('user_id'),
#                 # photos=','.join(data.getlist('photos'))
#             )
#             ad.title = f"{ad.car_brand} {ad.car_model} ({ad.car_year})"  # Устанавливаем title
#             ad.save()  # Сохраняем модель
#
#         elif category == 'realty':
#             ad = RealtyAd(
#                 ad_id=data.get('ad_id'),
#                 realty_deal=data.get('realty_deal'),
#                 # realty_type=data.get('realty_type'),
#                 # realty_square=data.get('realty_square'),
#                 # realty_rooms=data.get('realty_rooms'),
#                 # realty_floors_total=data.get('realty_floors_total'),
#                 # realty_floor=data.get('realty_floor'),
#                 # realty_currency=data.get('currency'),  # Передаем значение валюты
#                 # realty_price=data.get('realty_price'),  # Передаем цену
#                 # realty_location=data.get('realty_location'),
#                 # realty_contacts=data.get('realty_contacts'),
#                 # realty_name=data.get('realty_name'),
#                 # user_id=data.get('user_id'),
#                 # photos=','.join(data.getlist('photos'))
#             )
#             ad.title = ad.realty_deal  # Устанавливаем title
#             ad.save()  # Сохраняем модель
#
#         elif category == 'job':
#             ad = JobAd(
#                 ad_id=data.get('ad_id'),
#                 job_title=data.get('job_title'),
#                 # job_requirements=data.get('job_requirements'),
#                 # job_responsibilities=data.get('job_responsibilities'),
#                 # job_conditions=data.get('job_conditions'),
#                 # job_contacts=data.get('job_contacts'),
#                 # job_currency=data.get('currency'),  # Передаем значение валюты
#                 # job_price=data.get('job_price'),  # Передаем цену
#                 # job_name=data.get('job_name'),
#                 # user_id=data.get('user_id'),
#                 # photos=','.join(data.getlist('photos'))
#             )
#             ad.title = ad.job_title  # Устанавливаем title
#             ad.save()  # Сохраняем модель
#
#         else:
#             return HttpResponse("Unsupported category", status=400)
#
#         return HttpResponse("Data received successfully", status=200)
#
#     else:
#         return HttpResponse("Method not allowed", status=405)

# def display_cars(request):
#     car_brands = Car.objects.values_list('car_brand', flat=True).distinct()
#     car_models = Car.objects.values_list('car_model', flat=True).distinct()
#     car_years = Car.objects.values_list('car_year', flat=True).distinct()
#
#     selected_brand = request.GET.get('car_brand')
#     selected_model = request.GET.get('car_model')
#     selected_year = request.GET.get('car_year')
#
#     filtered_cars = Car.objects.all()
#
#     if selected_brand:
#         filtered_cars = filtered_cars.filter(car_brand=selected_brand)
#     if selected_model:
#         filtered_cars = filtered_cars.filter(car_model=selected_model)
#     if selected_year:
#         filtered_cars = filtered_cars.filter(car_year=selected_year)
#
#     all_cars = Car.objects.all().order_by('date_published')
#
#     return render(request, 'tgapi/adv.html', {'cars': all_cars, 'filtered_cars': filtered_cars, 'car_brands': car_brands, 'car_years': car_years, 'car_models': car_models})
#
# class CarDetailView(DetailView):
#     model = CarAd
#     template_name = 'tgapi/car_detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
#
#
#
# class RealtyListAPIView(APIView):
#     def get(self, request):
#         realty_data = self.get_realty_data()
#         job_data = self.get_job_data()
#         car_data = self.get_car_data()
#
#         # Merge data from different categories
#         merged_data = realty_data + job_data + car_data
#         print(merged_data)
#         return Response(merged_data)
#
#     def get_realty_data(self):
#         realties = Realty.objects.all()
#         realty_data = []
#
#         for realty in realties:
#             realty_data.append({
#                 'type': realty.realty_type,
#                 'user_id': realty.user_id,
#                 'ad_id': realty.ad_id,
#                 'deal': realty.realty_deal,
#                 'square': realty.realty_square,
#                 'photos': realty.photos,
#                 'date_published': realty.date_published.strftime('%Y-%m-%d %H:%M:%S')
#             })
#
#         return realty_data
#
#     def get_job_data(self):
#         jobs = Job.objects.all()
#         job_data = []
#
#         for job in jobs:
#             job_data.append({
#                 'type': 'job',
#                 'user_id': job.user_id,
#                 'ad_id': job.ad_id,
#                 'title': job.job_title,
#                 'requirements': job.job_requirements,
#                 'responsibilities': job.job_responsibilities,
#                 'conditions': job.job_conditions,
#                 'contacts': job.job_contacts,
#                 'photos': job.photos,
#                 'is_active': job.is_active
#             })
#
#         return job_data
#
#     def get_car_data(self):
#         cars = Car.objects.all()
#         car_data = []
#
#         for car in cars:
#             car_data.append({
#                 'type': 'car',
#                 'user_id': car.user_id,
#                 'ad_id': car.ad_id,
#                 'brand': car.car_brand,
#                 'model': car.car_model,
#                 'year': car.car_year,
#                 'body_type': car.car_body_type,
#                 'engine_type': car.car_engine_type,
#                 'engine_volume': car.car_engine_volume,
#                 'power': car.car_power,
#                 'transmission_type': car.car_transmission_type,
#                 'color': car.car_color,
#                 'mileage': car.car_mileage,
#                 'document_status': car.car_document_status,
#                 'owners': car.car_owners,
#                 'customs_cleared': car.car_customs_cleared,
#                 'condition': car.car_condition,
#                 'description': car.car_description,
#                 'currency': car.currency,
#                 'price': car.car_price,
#                 'location': car.car_location,
#                 'seller_name': car.seller_name,
#                 'seller_phone': car.seller_phone,
#                 'photos': car.photos,
#                 'date_published': car.date_published.strftime('%Y-%m-%d %H:%M:%S'),
#                 'is_active': car.is_active
#             })
#
#         return car_data



# @api_view(['GET'])
# def realty_list(request):
#     realtys = Realty.objects.all()
#     realty_data = list('json', realtys.values())
#     return JsonResponse(realty_data, safe=False)
