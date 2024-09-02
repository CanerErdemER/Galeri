
from django.contrib import admin
from django.urls import path
from Galeri import views


urlpatterns = [

    path('admin/', admin.site.urls),

    path("",views.index,name="arac_form"),
    
    path("arac/<slug:slug>",views.detaylar,name="arac_detay"),

    path("arac/<slug:slug>/edit",views.edit,name="arac_duzenle"),
    
    
      
]
