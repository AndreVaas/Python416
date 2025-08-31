from django.urls import path
from . import views

urlpatterns = [
    path('', views.apartment, name='apartment'),
    path('apartment/<int:pk>/', views.apartment_detail, name='apartment_detail'),
    path('apartment/new/', views.apartment_create, name='apartment_create'),
    path('signup/', views.signup_user, name='signupuser'),
    path('login/', views.login_user, name='loginuser'),
    path('logout/', views.logout_user, name='logoutuser'),
    path('apartment/<int:apartment_id>/room/new/', views.room_create, name='room_create'),
    path('room/<int:room_id>/work/new/', views.work_create, name='work_create'),
]
