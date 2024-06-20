from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_view, name='search_results'),
    # Добавьте другие пути при необходимости
]