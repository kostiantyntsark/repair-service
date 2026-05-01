from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegisterForm, LoginForm


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('/')
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    form = LoginForm(data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('/')
    return render(request, 'users/login.html', {'form': form})


def user_logout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('/')