from django import forms
from django.forms import ModelForm
from .models import Arabalar

class ArabalarForm(ModelForm):
    class Meta:
        model=Arabalar
        fields=["Marka_Model","Fiyat","Plaka"]


    
