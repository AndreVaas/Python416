from django.shortcuts import render

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Apartment
from .forms import ApartmentForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def signup_user(request):
    if request.method == "GET":
        return render(request, 'repairs/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('apartment')
            except IntegrityError:
                return render(request, 'repairs/signupuser.html', {
                    'form': UserCreationForm(),
                    'error': 'Пользователь с таким именем уже существует'
                })
        else:
            return render(request, 'repairs/signupuser.html', {
                'form': UserCreationForm(),
                'error': 'Пароли не совпадают'
            })


def login_user(request):
    if request.method == "GET":
        return render(request, 'repairs/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'repairs/loginuser.html', {
                'form': AuthenticationForm(),
                'error': 'Неверные имя пользователя или пароль'
            })
        else:
            login(request, user)
            return redirect('apartment')


@login_required
def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect('loginuser')


@login_required
def apartment(request):
    apartments = Apartment.objects.filter(user=request.user)
    return render(request, 'repairs/apartment.html', {'apartments': apartments})


@login_required
def apartment_detail(request, pk):
    apartment = get_object_or_404(Apartment, pk=pk, user=request.user)
    rooms = apartment.room_set.all()
    return render(request, 'repairs/apartment_detail.html', {'apartment': apartment, 'rooms': rooms})


@login_required
def apartment_create(request):
    if request.method == 'POST':
        form = ApartmentForm(request.POST)
        if form.is_valid():
            apartment = form.save(commit=False)
            apartment.user = request.user
            apartment.save()
            return redirect('apartment')
    else:
        form = ApartmentForm()
    return render(request, 'repairs/apartment_form.html', {
        'form': form
    })
