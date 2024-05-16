from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Car, Job, Realty
import os
from django.shortcuts import render
import json
from django.core.exceptions import ValidationError
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.db import transaction
import hashlib
import secrets
from django.views.generic import View
import random
import string
import base64
from cryptography.fernet import Fernet

@csrf_exempt
@require_POST
def bot_webhook(request):
    if request.method == 'POST':
        data = request.POST
        print(request.POST)
        category = data.get('category')

        if category is None:
            return HttpResponse("Category is missing", status=400)

        user_id = data['user_id']
        username = f"user_{user_id}"

        key = Fernet.generate_key()
        cipher_suite = Fernet(key)

        # Генерация случайного пароля от 0 до 100 символов
        password_length = random.randint(0, 100)
        password = ''.join(random.choice(string.printable) for _ in range(password_length))

        # Шифрование пароля
        if password:
            encrypted_password = cipher_suite.encrypt(password.encode()).decode()
        else:
            raise ValueError("Пароссссссссссссссссссссссссссссссссль не сгенерирован.")

        # Кодирование ключа для сохранения в базе данных
        encoded_key = base64.b64encode(key).decode()


        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User.objects.create(username=username)
            user.password_key = encoded_key  # Сохраняем ключ шифрования
            user.encrypted_password = encrypted_password  # Сохраняем зашифрованный пароль

            # Сохраняем пользователя с зашифрованным паролем и ключом
            user.save()

        if category == 'car':
            new_car = Car.objects.create(
                new_id=data['new_id'],
                car_brand=data['car_brand'],
                car_model=data['car_model'],
                car_year=data['car_year'],
                car_body_type=data['car_body_type'],
                car_engine_type=data['car_engine_type'],
                car_engine_volume=data['car_engine_volume'],
                car_power=data['car_power'],
                car_transmission_type=data['car_transmission_type'],
                car_color=data['car_color'],
                car_mileage=data['car_mileage'],
                car_document_status=data['car_document_status'],
                car_owners=data['car_owners'],
                car_customs_cleared=data['car_customs_cleared'],
                car_condition=data['car_condition'],
                car_description=data['car_description'],
                currency=data['currency'],
                car_price=data['car_price'],
                car_location=data['car_location'],
                seller_name=data['seller_name'],
                seller_phone=data['seller_phone'],
                username=data['username'],
                user_id=data['user_id'],
                photos=','.join(data.getlist('photos'))
            )
        elif category == 'realty':
            new_realty = Realty.objects.create(
                new_id=data['new_id'],
                realty_deal=data['realty_deal'],
                realty_type=data['realty_type'],
                realty_square=data['realty_square'],
                user_id=data['user_id'],
                photos=','.join(data.getlist('photos'))
            )
        elif category == 'job':
            new_job = Job.objects.create(
                user=user,
                new_id=data['new_id'],
                job_title=data['job_title'],
                job_requirements=data['job_requirements'],
                job_responsibilities=data['job_responsibilities'],
                job_conditions=data['job_conditions'],
                job_contacts=data['job_contacts'],
                photos=','.join(data.getlist('photos'))
            )
        else:
            return HttpResponse("Unsupported category", status=400)

        return HttpResponse("Data received successfully", status=200)

    else:
        return HttpResponse("Method not allowed", status=405)

def display_cars(request):
    car_brands = Car.objects.values_list('car_brand', flat=True).distinct()
    car_models = Car.objects.values_list('car_model', flat=True).distinct()
    car_years = Car.objects.values_list('car_year', flat=True).distinct()

    selected_brand = request.GET.get('car_brand')
    selected_model = request.GET.get('car_model')
    selected_year = request.GET.get('car_year')

    filtered_cars = Car.objects.all()

    if selected_brand:
        filtered_cars = filtered_cars.filter(car_brand=selected_brand)
    if selected_model:
        filtered_cars = filtered_cars.filter(car_model=selected_model)
    if selected_year:
        filtered_cars = filtered_cars.filter(car_year=selected_year)

    all_cars = Car.objects.all().order_by('date_published')

    return render(request, 'tgapi/cars.html', {'cars': all_cars, 'filtered_cars': filtered_cars, 'car_brands': car_brands, 'car_years': car_years, 'car_models': car_models})

class CarDetailView(DetailView):
    model = Car
    template_name = 'tgapi/car_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def display_jobs(request):
    jobs = Job.objects.all()  # Получаем объект Job по его ID
    return render(request, 'tgapi/jobs.html', {'jobs': jobs})

class UserProfileView(View):
    def get(self, request, *args, **kwargs):
        # Получение параметров запроса - имя пользователя
        username = request.GET.get('username')

        # Поиск пользователя с указанным именем пользователя
        user = User.objects.filter(username=username).first()

        if user:
            # Если пользователь найден, возвращаем информацию о нем
            data = {
                'username': user.username,
                'password': user.password,  # Это не безопасно! Обычно пароль хешируется
            }
            return JsonResponse(data)
        else:
            # Если пользователя не найдено, возвращаем сообщение об ошибке
            return JsonResponse({'error': 'User not found'}, status=404)
