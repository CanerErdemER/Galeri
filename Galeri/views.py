from django.shortcuts import render
from .models import Arabalar

# Create your views here.

def index(request):
    sayfa='index.html'
    ctx={'arabalar':Arabalar.objects.all()}  
    return render(request,sayfa,ctx)

def detaylar(request,slug):
    sayfa='aracdetay.html'
    ctx={'aracdetay':Arabalar.objects.get(slug=slug)}
    
    return render(request,sayfa,ctx)


# def detail(request,id):
#     tema = 'home.html'
#     context = {'ogrenci' : OgrenciModeli.objects.get(id=id)}

#     return render(request, tema, context)
    
    
    

