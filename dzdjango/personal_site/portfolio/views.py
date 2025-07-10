from django.shortcuts import render


def portfolio(request):
    return render(request, "personal_site/portfolio.html", {'portfolio': portfolio})