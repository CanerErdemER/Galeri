from django import forms
from django.forms import ModelForm
from .models import Arabalar

class ArabalarForm(forms.Form):
    plaka=forms.CharField(label="Plakanız",max_length=20)
    model=forms.CharField(label="marka model")
    fiyat=forms.IntegerField()


    
