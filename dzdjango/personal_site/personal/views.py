from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Personal
from .forms import BlogForm


def index(request):
    projects = Personal.objects.all()
    return render(request, 'personal/index.html', {'projects': projects})


def portfolio(request):
    return render(request, "personal/portfolio.html", {'portfolio': portfolio})


def signup_user(request):
    if request.method == "GET":
        return render(request, 'personal/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'personal/signupuser.html',
                              {'form': UserCreationForm(),
                               'error': 'Такое имя пользователя существует, задайте другое'})

        else:
            return render(request, 'personal/signupuser.html',
                          {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')


def login_user(request):
    if request.method == "GET":
        return render(request, "personal/loginuser.html", {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is None:
        return render(request, "personal/loginuser.html", {
            'form': AuthenticationForm(),
            'error': 'Неверные данные для входа'})
    else:
        login(request, user)
        return redirect('index')


def create_otz(request):
    if request.method == "GET":
        return render(request, "personal/createotz.html", {"form": BlogForm()})
    else:
        try:
            form = BlogForm(request.POST)
            new_otz = form.save(commit=False)
            new_otz.user = request.user
            new_otz.save()
            return redirect('blogs')
        except ValueError:
            return render(request, 'personal/createotz.html',
                          {
                              "form": BlogForm(), 'error': 'Переданы неверные данные'})
