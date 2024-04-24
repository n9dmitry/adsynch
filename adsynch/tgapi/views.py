from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import CarAd, JobAd, RealtyAd
import os
from django.shortcuts import render
import json
from django.core.exceptions import ValidationError
from django.views.generic import DetailView


@csrf_exempt
@require_POST
def bot_webhook(request):
    if request.method == 'POST':
        data = request.POST
        print(request.POST)
        category = data.get('category')

        if category is None:
            return HttpResponse("Category is missing", status=400)

        if category == 'car':
            new_car = Car.objects.create(
                ad_id=data['ad_id'],
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
                ad_id=data['ad_id'],
                realty_deal=data['realty_deal'],
                realty_type=data['realty_type'],
                realty_square=data['realty_square'],
                user_id=data['user_id'],
                photos=','.join(data.getlist('photos'))
            )
        elif category == 'job':
            new_job = Job.objects.create(
                ad_id=data['ad_id'],
                job_title=data['job_title'],
                job_requirements=data['job_requirements'],
                job_responsibilities=data['job_responsibilities'],
                job_conditions=data['job_conditions'],
                job_contacts=data['job_contacts'],
                user_id=data['user_id'],
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

    return render(request, 'tgapi/adv.html', {'cars': all_cars, 'filtered_cars': filtered_cars, 'car_brands': car_brands, 'car_years': car_years, 'car_models': car_models})

class CarDetailView(DetailView):
    model = CarAd
    template_name = 'tgapi/car_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class RealtyListAPIView(APIView):
    def get(self, request):
        realty_data = self.get_realty_data()
        job_data = self.get_job_data()
        car_data = self.get_car_data()

        # Merge data from different categories
        merged_data = realty_data + job_data + car_data
        print(merged_data)
        return Response(merged_data)

    def get_realty_data(self):
        realties = Realty.objects.all()
        realty_data = []

        for realty in realties:
            realty_data.append({
                'type': realty.realty_type,
                'user_id': realty.user_id,
                'ad_id': realty.ad_id,
                'deal': realty.realty_deal,
                'square': realty.realty_square,
                'photos': realty.photos,
                'date_published': realty.date_published.strftime('%Y-%m-%d %H:%M:%S')
            })

        return realty_data

    def get_job_data(self):
        jobs = Job.objects.all()
        job_data = []

        for job in jobs:
            job_data.append({
                'type': 'job',
                'user_id': job.user_id,
                'ad_id': job.ad_id,
                'title': job.job_title,
                'requirements': job.job_requirements,
                'responsibilities': job.job_responsibilities,
                'conditions': job.job_conditions,
                'contacts': job.job_contacts,
                'photos': job.photos,
                'is_active': job.is_active
            })

        return job_data

    def get_car_data(self):
        cars = Car.objects.all()
        car_data = []

        for car in cars:
            car_data.append({
                'type': 'car',
                'user_id': car.user_id,
                'ad_id': car.ad_id,
                'brand': car.car_brand,
                'model': car.car_model,
                'year': car.car_year,
                'body_type': car.car_body_type,
                'engine_type': car.car_engine_type,
                'engine_volume': car.car_engine_volume,
                'power': car.car_power,
                'transmission_type': car.car_transmission_type,
                'color': car.car_color,
                'mileage': car.car_mileage,
                'document_status': car.car_document_status,
                'owners': car.car_owners,
                'customs_cleared': car.car_customs_cleared,
                'condition': car.car_condition,
                'description': car.car_description,
                'currency': car.currency,
                'price': car.car_price,
                'location': car.car_location,
                'seller_name': car.seller_name,
                'seller_phone': car.seller_phone,
                'photos': car.photos,
                'date_published': car.date_published.strftime('%Y-%m-%d %H:%M:%S'),
                'is_active': car.is_active
            })

        return car_data



# @api_view(['GET'])
# def realty_list(request):
#     realtys = Realty.objects.all()
#     realty_data = list('json', realtys.values())
#     return JsonResponse(realty_data, safe=False)
