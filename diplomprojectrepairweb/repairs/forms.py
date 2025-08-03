from django import forms
from .models import Apartment


class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['name', 'address', 'total_area']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'total_area': forms.NumberInput(attrs={'class': 'form-control'}),
        }
