from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import CarAdView, RealtyAdView, JobAdView, my_ads, profile_view, check_user, generate_link
from .views import CarAdListView, RealtyAdListView, JobAdListView, get_models

import logging
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path("car_ad/", CarAdView.as_view()),
    path("realty_ad/", RealtyAdView.as_view()),
    path("job_ad/", JobAdView.as_view()),
    path('cars', CarAdListView.as_view(), name='cars'),
    path('realty', RealtyAdListView.as_view(), name='realty'),
    path('jobs', JobAdListView.as_view(), name='jobs'),

    path('car/<int:pk>/', views.CarAdDetailView.as_view(), name='car-detail'),
    path('job/<int:pk>/', views.JobAdDetailView.as_view(), name='job-detail'),
    path('realty/<int:pk>/', views.RealtyAdDetailView.as_view(), name='realty-detail'),
    path('my_ads/<str:username>/', views.my_ads, name='my_ads'),
    path('check_user/<str:username>/', views.check_user, name='check_user'),
    path('<str:username>/<str:token>/', views.profile_view, name='profile_view'),
    path('generate_link/', views.generate_link, name='generate_link'),
    path('get-models/', get_models, name='get_models'),
    path('get_currency_rate/', views.get_currency_rate, name='get_currency_rate'),
    # path('car_ads/', CarAdListView.as_view(), name='car_ad_list'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)