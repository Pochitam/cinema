from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from core.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    if request.method == 'POST':
        # Получаем загруженный файл
        avatar = request.FILES.get('avatar')
        if avatar:
            # Обновляем аватарку в профиле
            profile = request.user
            profile.photo = avatar
            profile.save()
    return render(request, 'core/profile.html')

def sign_in(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'core/sign_in.html', {'error': 'Неверный логин или пароль'})
    return render(request, 'core/sign_in.html')


def sign_up(request):
    if request.method=='POST':
        login = request.POST['login']
        password = request.POST['password']
        password_repeat = request.POST.get('password_repeat')
        if password!=password_repeat:
            return render(request, 'core/sign_up.html', {'error': 'Пароли не совпадают'})
        User.objects.create_user(
            username = login,
            password = password
        )
        return redirect('sign_in')
    return render(request, 'core/sign_up.html')
