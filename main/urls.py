
from django.contrib import admin
from django.urls import path
from Galeri import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("",views.arac_Cek,name="arac_form"),
   
    path("<int:arac_id>",views.arac_Cek,name="arac_form"),
    
    path("arac/<slug:slug>",views.detaylar,name="arac_detay"),
    
    
      
]
