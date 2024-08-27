from django.contrib import admin
from .models import Arabalar


# Register your models here.


@admin.register(Arabalar)
class ArabalarAdmin(admin.ModelAdmin):
    list_display = ['Plaka','slug']

