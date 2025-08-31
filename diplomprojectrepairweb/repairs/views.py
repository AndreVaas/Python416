from django.shortcuts import render

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Apartment, Room, Work
from .forms import ApartmentForm, RoomForm, WorkForm
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


@login_required
def room_create(request, apartment_id):
    apartment = get_object_or_404(Apartment, pk=apartment_id, user=request.user)
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.apartment = apartment
            room.save()
            return redirect('apartment_detail', pk=apartment.id)
    else:
        form = RoomForm()
    return render(request, 'repairs/room_form.html', {'form': form, 'apartment': apartment})


@login_required
def work_create(request, room_id):
    room = get_object_or_404(Room, pk=room_id, apartment__user=request.user)
    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            work = form.save(commit=False)
            work.room = room
            work.save()
            return redirect('apartment_detail', pk=room.apartment.id)
    else:
        form = WorkForm()
    return render(request, 'repairs/work_form.html', {'form': form, 'room': room})
