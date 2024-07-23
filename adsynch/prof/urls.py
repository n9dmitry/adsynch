from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
# from .views import forgot_password
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.profile, name='profile'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

