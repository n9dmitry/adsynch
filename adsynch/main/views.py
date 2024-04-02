from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages




def index(request):
    return render(request, 'main/index.html',)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            # Создаем пользователя
            user = User.objects.create_user(username, email, password)
            user.save()
            messages.success(request, 'Пользователь успешно зарегистрирован!')
            return redirect('home')  # перенаправить на вашу главную страницу
        else:
            # Если форма невалидна, передаем ошибки в шаблон
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
            return render(request, 'main/index.html', {'form': form})
    # else:
    #     form = RegistrationForm()
    # return render(request, 'main/index.html', {'form': form})