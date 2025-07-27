from django.db import models
from django.contrib.auth.models import User


# Название проекта(Квартира, частный дом) добавил 27.07.25
class Apartment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True)
    total_area = models.FloatField()

    def __str__(self):
        return self.name
