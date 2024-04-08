from django.urls import path

from .views import UserDataAPIView

urlpatterns = [
    path("api/user_data/", UserDataAPIView.as_view()),
]