
from django.contrib import admin
from django.urls import path
from Galeri import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path("arac/<slug:slug>",views.detaylar,name="arac_detay"),
    path("aracform/",views.arac_Cek,name="arac_form")
    
      
]
