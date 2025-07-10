from django.shortcuts import render
from .models import Personal


def index(request):
    projects = Personal.objects.all()
    return render(request, 'personal/index.html', {'projects': projects})


def portfolio(request):
    return render(request, "personal/portfolio.html", {'portfolio': portfolio})
