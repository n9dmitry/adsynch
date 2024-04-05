# Стандартные Django-импорты
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
# Импорты из проекта
from .forms import RegistrationForm
# Внешние библиотеки
import uuid
from transliterate import translit





def index(request):
    return render(request, 'main/index.html',)


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
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
            print(form.errors.as_data())

    else:
        form = RegistrationForm()
        print('3')
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