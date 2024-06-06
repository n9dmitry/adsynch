from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("main.urls"), name='index'),

    path('admin/', admin.site.urls),
    path(r'^ckeditor/', include("ckeditor_uploader.urls")),
    path('api/', include('tgapi.urls')),  # Добавьте эту строку
    path('ads/', include('tgapi.urls')),  # Добавьте эту строку
    path('blog/', include('blog.urls')),  # Добавьте эту строку
    path('', include('tgapi.urls')),  # Добавьте эту строку
]


# from django.contrib import admin
# from django.urls import path, include
#
# from django.conf.urls.static import static
# from django.conf import settings
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include("main.urls"), name='index'),
#     path('store/', include("store.urls"), name='store'),
#     path('category/', include("category.urls"), name='category'),
#     path('news/', include("news.urls"), name='news'),
#     path('feedback/', include("feedback.urls"), name='feedback'),
#     path('grappelli/', include('grappelli.urls')),
#     path(r'^ckeditor/', include("ckeditor_uploader.urls")),
#
#
# ]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)