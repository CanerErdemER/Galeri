
from django.contrib import admin
from django.urls import path
from Galeri import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path("Arac/<slug:slug>",views.detaylar,name="arac_detay")
      
]
