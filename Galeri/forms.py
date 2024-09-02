from django import forms
from django.forms import ModelForm
from .models import Arabalar

class ArabalarForm(forms.Form):
    plaka=forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"Plaka Girin",
        "class":"form-control",
        }))
    model=forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"Marka Model",
        "class":"form-control",
        }))
    fiyat=forms.IntegerField(widget=forms.NumberInput(attrs={
        "placeholder":"Fiyat Girin",
        "class":"form-control",
        }))
    


    
