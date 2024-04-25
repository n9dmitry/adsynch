from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import CarAdView, RealtyAdView, JobAdView


urlpatterns = [
    # path("user_data/", views.bot_webhook),  # Обратите внимание на двоеточие после views
    path("car_ad/", CarAdView.as_view(), name='car_ad'),
    path("realty_ad/", RealtyAdView.as_view(), name='realty_ad'),
    path("job_ad/", JobAdView.as_view(), name='job_ad'),
    # path("realty_ad/", views.realty_webhook),
    # path("job_ad/", views.job_webhook),


    # path("myads/", views.RealtyListAPIView.as_view()),  # Обратите внимание на двоеточие после views
    # path('', views.display_cars, name='cars'),
    # path('/<int:pk>', views.CarDetailView.as_view(), name='car_detail'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)