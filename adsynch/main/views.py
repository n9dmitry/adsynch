import uuid
from transliterate import translit

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User

from tgapi.models import Ads, CarAd, JobAd, RealtyAd, UserProfile
from blog.models import Article
from .forms import RegistrationForm
from .models import AboutPage, ServicesPage, Bnr, SliderImage
# from .forms import CustomPasswordResetForm
import random


import uuid
from transliterate import translit

def index(request):
    car_ad = CarAd.objects.all()
    realty_ad = RealtyAd.objects.all()
    job_ad = JobAd.objects.all()
    published_articles = Article.objects.filter(published=True)

    banners_top = Bnr.objects.filter(position='top')
    banners_center = Bnr.objects.filter(position='center')
    banners_bottom = Bnr.objects.filter(position='bottom')

    # Получение топ-4 объявлений по просмотрам для каждой категории
    top_car_ads = CarAd.objects.order_by('-views')[:5]
    top_realty_ads = RealtyAd.objects.order_by('-views')[:5]
    top_job_ads = JobAd.objects.order_by('-views')[:5]

    # Объединение всех объявлений в один список
    recommendation_listing = list(top_car_ads) + list(top_realty_ads) + list(top_job_ads)
    random.shuffle(recommendation_listing)
    slider_images = SliderImage.objects.all()

    context = {
        'car_ad': car_ad,
        'realty_ad': realty_ad,
        'job_ad': job_ad,
        'published_articles': published_articles,
        'banners_top': banners_top,
        'banners_center': banners_center,
        'banners_bottom': banners_bottom,
        'recommendation_listing': recommendation_listing,  # Добавляем топ-12 объявлений в контекст
        'slider_images': slider_images
    }

    return render(request, 'main/index.html', context)

def services(request):
    service_pages = ServicesPage.objects.all()
    return render(request, 'main/services.html', {'service_pages': service_pages})

def contacts(request):
    return render(request, 'main/contact.html')

def about(request):
    about_pages = AboutPage.objects.all()
    return render(request, 'main/about.html', {'about_pages': about_pages})

@login_required
def my_items(request, username):

    if username:
        active_car_ads = CarAd.objects.filter(is_active=True, user__username=username)
        inactive_car_ads = CarAd.objects.filter(is_active=False, user__username=username)
        active_realty_ads = RealtyAd.objects.filter(is_active=True, user__username=username)
        inactive_realty_ads = RealtyAd.objects.filter(is_active=False, user__username=username)
        active_job_ads = JobAd.objects.filter(is_active=True, user__username=username)
        inactive_job_ads = JobAd.objects.filter(is_active=False, user__username=username)
        context = {
            'active_car_ads': active_car_ads,
            'inactive_car_ads': inactive_car_ads,
            'active_realty_ads': active_realty_ads,
            'inactive_realty_ads': inactive_realty_ads,
            'active_job_ads': active_job_ads,
            'inactive_job_ads': inactive_job_ads,
        }
    else:
        return render(request, 'error_page.html', {'message': 'Username is required'})

    return render(request, 'main/my_items.html', context)

def products(request):
    car_ad = CarAd.objects.all()
    realty_ad = RealtyAd.objects.all()
    job_ad = JobAd.objects.all()

    return render(request, 'main/products.html', {'car_ad': car_ad, 'realty_ad': realty_ad, 'job_ad': job_ad})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            # Проверяем, существует ли пользователь с таким email
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Пользователь с таким email уже существует.')
                return render(request, 'main/index.html', {'form': form})

            username = translit(name, reversed=True)
            username = username.lower()
            username += '.' + str(uuid.uuid4().hex)[:6]

            user = User.objects.create_user(username, email, password)
            user.save()
            messages.success(request, 'Пользователь успешно зарегистрирован!')
            return redirect('index')
        else:
            error_messages = '\n'.join([f'{field}: {", ".join(errors)}' for field, errors in form.errors.items()])
            messages.error(request, f'Пожалуйста, исправьте ошибки в форме:\n{error_messages}')



    else:
        form = RegistrationForm()
    return render(request, 'main/index.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print("Received email:", email)  # Отладочное сообщение для проверки полученного email
        print("Received password:", password)  # Отладочное сообщение для проверки полученного пароля

        # Проверяем наличие пользователя в базе данных
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        # Если пользователь существует, проверяем правильность пароля
        if user is not None and user.check_password(password):
            login(request, user)
            print("User authenticated successfully:", user)  # Отладочное сообщение для проверки успешной аутентификации пользователя
            # Здесь можно добавить перенаправление на другую страницу после успешного входа
            return redirect('index')
        else:
            messages.error(request, 'Неверный email или пароль')
            return render(request, 'main/index.html')
    return render(request, 'main/index.html')

def logout_view(request):
    auth_logout(request)
    return redirect('index')

# понадобится при регистрации
# def forgot_password(request):
#     if request.method == 'POST':
#         form = PasswordResetForm(request.POST)
#         if form.is_valid():
#             form.save(request=request)
#             email = form.cleaned_data.get('email')  # Получаем адрес электронной почты из формы
#             token = form.cleaned_data.get('token')  # Получаем токен из формы (если он нужен)
#
#             # Отправляем письмо с токеном на адрес электронной почты
#             send_mail(
#                 'Восстановление пароля',  # Тема письма
#                 'Ваш токен для восстановления пароля: {}'.format(token),  # Текст письма
#                 'your_email@example.com',  # Адрес отправителя
#                 [email],  # Адреса получателей
#                 fail_silently=False,  # Не игнорировать ошибки при отправке
#             )
#
#             messages.success(request, 'Инструкции по сбросу пароля были отправлены на ваш адрес электронной почты.')
#             return redirect('login')  # Перенаправление на страницу входа после отправки инструкций
#     else:
#         form = CustomPasswordResetForm()
#     return render(request, 'main/forgot_password.html', {'form': form})

@login_required
def my_ads_view(request):
    user = request.user
    car_ads = CarAd.objects.filter(user=user)
    realty_ads = RealtyAd.objects.filter(user=user)
    job_ads = JobAd.objects.filter(user=user)


    context = {
        'active_car_ads': car_ads.filter(is_active=True),
        'inactive_car_ads': car_ads.filter(is_active=False),
        'active_realty_ads': realty_ads.filter(is_active=True),
        'inactive_realty_ads': realty_ads.filter(is_active=False),
        'active_job_ads': job_ads.filter(is_active=True),
        'inactive_job_ads': job_ads.filter(is_active=False),
    }

    return render(request, 'main/my_ads.html', context)

@login_required
def profile(request):
    user_profile = UserProfile.objects.first()  # Получаем первый объект UserProfile (ваша логика получения профиля пользователя может отличаться)
    return render(request, 'main/profile.html', {'user_profile': user_profile})