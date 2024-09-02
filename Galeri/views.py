from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .models import Arabalar
from .forms import ArabalarForm

# Create your views here.

def index(request):
    sayfa='index.html'
    ctx={'arabalar':Arabalar.objects.all()}  
    return render(request,sayfa,ctx)

def detaylar(request,slug):
    sayfa='aracdetay.html'
    ctx={'aracdetay':Arabalar.objects.get(slug=slug)}
    
    return render(request,sayfa,ctx)

def edit(request,slug):
    if request.method == "POST":
        form = ArabalarForm(request.POST)
        if form.is_valid():
            # # Plaka Marka_Model Fiyat modelsten geliyor
            
            plaka=form.cleaned_data["plaka"]   
            model=form.cleaned_data["model"] 
            fiyat=form.cleaned_data["fiyat"]
            

            ahmet=Arabalar(Plaka=plaka,Marka_Model=model,Fiyat=fiyat)
            ahmet.save()
            return redirect("arac_form")                      
    else:
        form = ArabalarForm()
    return render(request, "aracduzenle.html", {"form": form,'arabalar':Arabalar.objects.all()})





    
    
    

