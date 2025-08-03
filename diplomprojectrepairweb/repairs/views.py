from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Apartment
from .forms import ApartmentForm

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
            return redirect('apartment_list')
    else:
        form = ApartmentForm()
    return render(request, 'repairs/apartment_form.html', {
        'form': form
    })
