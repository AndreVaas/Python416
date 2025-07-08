from django.shortcuts import render
from .models import Personal


def index(request):
    projects = Personal.objects.all()
    return render(request, 'personal/index.html', {'projects': projects})
