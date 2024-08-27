from django.shortcuts import render
from .models import ArabalarModeli

# Create your views here.

def index(request):
    sayfa='index.html'
    ctx={'arabalar':ArabalarModeli.objects.all()}
    
    return render(request,sayfa,ctx)

def detaylar(request,arac_id):
    arac={'aracdetay':ArabalarModeli.objects.get(arac_id=arac_id)}
    
    
    

