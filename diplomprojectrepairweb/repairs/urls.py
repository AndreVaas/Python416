from django.urls import path
from . import views

urlpatterns = [
    path('', views.apartment, name='apartment'),
    path('apartment/<int:pk>/', views.apartment_detail, name='apartment_detail'),
]