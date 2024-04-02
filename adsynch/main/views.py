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
            # username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            # Создаем пользователя
            username = translit(name, reversed=True)  # Транслитерация имени в lowercase
            username += '.' + str(uuid.uuid4().hex)[:6]  # Добавляем уникальный идентификатор

            user = User.objects.create_user(username, email, password)
            print('username', username)
            user.save()
            messages.success(request, 'Пользователь успешно зарегистрирован!')
            print('1')
            return redirect('index')  # перенаправить на вашу главную страницу
        else:
            # Если форма невалидна, передаем ошибки в шаблон
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
            print(form.errors.as_data())

    else:
        form = RegistrationForm()
        print('3')
    return render(request, 'main/index.html', {'form': form})