from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .models import Arabalar
from .forms import ArabalarForm

# Create your views here.


    

def detaylar(request,slug):
    sayfa='aracdetay.html'
    ctx={'aracdetay':Arabalar.objects.get(slug=slug)}
    
    return render(request,sayfa,ctx)

def arac_Cek(request):

    sayfa='index.html'
    ctx={'arabalar':Arabalar.objects.all()}  
    
    if request.method == "POST":
        form = ArabalarForm(request.POST)
        if form.is_valid():
            # # Plaka Marka_Model Fiyat modelsten geliyor
            plaka=form.cleaned_data["plaka"]   
            model=form.cleaned_data["model"] 
            fiyat=form.cleaned_data["fiyat"]
            

            ahmet=Arabalar(Plaka=plaka,Marka_Model=model,Fiyat=fiyat)
            ahmet.save()
            return redirect("arac_form", )                      
    else:
        # if arac_id:
        #     arac=Arabalar.objects.get(id=arac_id)
        #     form=ArabalarForm(initial={
        #         "plaka":arac.Plaka,
        #         "model":arac.Marka_Model,
        #         "plaka":arac.Fiyat,

        #     })
        # else:
            form=ArabalarForm()
    return render(request, "index.html", {"form": form,'arabalar':Arabalar.objects.all()})









    
    
    

