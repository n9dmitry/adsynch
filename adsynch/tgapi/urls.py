from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import CarAdView, RealtyAdView, JobAdView, check_user, generate_link, profile_view, my_ads

urlpatterns = [
    # path("user_data/", views.bot_webhook),  # Обратите внимание на двоеточие после views
    path("car_ad/", views.CarAdView.as_view()),
    path("realty_ad/", views.RealtyAdView.as_view()),
    path("job_ad/", views.JobAdView.as_view()),
    path('myads/<str:username>/', views.my_ads, name='my_ads'),  # Переместите этот маршрут вверх
    path('check_user/<str:username>/', views.check_user, name='check_user'),
    path('<str:username>/<str:token>/', views.profile_view, name='profile_view'),  # Этот маршрут должен быть ниже
    path('generate_link/', views.generate_link, name='generate_link'),
    # path('', views.display_cars, name='cars'),
    # path('/<int:pk>', views.CarDetailView.as_view(), name='car_detail'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)