from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages
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
            # Создаем пользователя
            username = translit(name.lower(), reversed=True)  # Транслитерация имени в lowercase
            username += '.' + str(uuid.uuid4().hex)[:6]  # Добавляем уникальный идентификатор

            user = User.objects.create_user(name, username, email, password)
            user.save()
            messages.success(request, 'Пользователь успешно зарегистрирован!')
            return redirect('index')  # перенаправить на вашу главную страницу
        else:
            # Если форма невалидна, передаем ошибки в шаблон
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = RegistrationForm()
    return render(request, 'main/index.html', {'form': form})