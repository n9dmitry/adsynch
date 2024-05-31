from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import CarAdView, RealtyAdView, JobAdView

urlpatterns = [
    # path("user_data/", views.bot_webhook),  # Обратите внимание на двоеточие после views
    path("car_ad/", CarAdView.as_view()),
    path("realty_ad/", RealtyAdView.as_view()),
    path("job_ad/", JobAdView.as_view()),
    path('cars', views.cars, name='cars'),
    path('car/<int:pk>/', views.CarAdDetailView.as_view(), name='carad-detail'),
    path('jobs', views.jobs, name='jobs'),
    path('jobs/<int:pk>/', views.JobAdDetailView.as_view(), name='jobs-detail'),
    path('realty', views.realtys, name='realty'),
    path('realty_ad/<int:pk>/', views.RealtyAdDetailView.as_view(), name='realty_detail'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)