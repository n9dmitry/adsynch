from django.urls import path
from . import views

urlpatterns = [
    path("user_data/", views.bot_webhook),  # Обратите внимание на двоеточие после views
]
