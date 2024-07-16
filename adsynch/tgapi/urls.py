from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import CarAdView, RealtyAdView, JobAdView, my_ads, profile_view, check_user, generate_link
from .views import CarAdListView, RealtyAdListView, JobAdListView, get_models
import logging
import debug_toolbar
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path("car_ad/", CarAdView.as_view()),
    path("realty_ad/", RealtyAdView.as_view()),
    path("job_ad/", JobAdView.as_view()),
    path('cars', CarAdListView.as_view(), name='cars'),
    path('realty', RealtyAdListView.as_view(), name='realty'),
    path('jobs', JobAdListView.as_view(), name='jobs'),

    path('car/(?P<pk>[0-9]+)/\\Z', views.CarAdDetailView.as_view(), name='carad-detail'),
    path('jobs/(?P<pk>[0-9]+)/\\Z', views.JobAdDetailView.as_view(), name='jobs-detail'),
    path('realty/(?P<pk>[0-9]+)/\\Z', views.RealtyAdDetailView.as_view(), name='realty_detail'),
    path('my_ads/<str:username>/', views.my_ads, name='my_ads'),
    path('check_user/<str:username>/', views.check_user, name='check_user'),
    path('<str:username>/<str:token>/', views.profile_view, name='profile_view'),
    path('generate_link/', views.generate_link, name='generate_link'),
    path('get-models/', get_models, name='get_models'),
    path('get_currency_rate/', views.get_currency_rate, name='get_currency_rate'),
    # path('car_ads/', CarAdListView.as_view(), name='car_ad_list'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
