from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum, F, DecimalField

class Apartment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True)
    total_area = models.FloatField()

    def __str__(self):
        return self.name

    def works_cost(self):
        rooms = self.room_set.all()
        return sum(room.work_set.aggregate(total_cost=Sum('cost'))['total_cost'] or 0 for room in rooms)

    def materials_cost(self):
        rooms = self.room_set.all()
        return sum(room.material_set.aggregate(total_cost=Sum(F('cost') * F('quantity'), output_field=DecimalField()))['total_cost'] or 0 for room in rooms)

    def total_cost(self):
        return self.works_cost() + self.materials_cost()

class Room(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    area = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.apartment.name})"

class Work(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.name

class Material(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=20)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name