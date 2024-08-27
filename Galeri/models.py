from django.db import models
from django import forms
# Create your models here.
from autoslug import AutoSlugField
class Arabalar(models.Model):

    Marka_Model=models.CharField(max_length=50)
    Fiyat=models.IntegerField()
    Plaka=models.CharField(max_length=20)
    slug = AutoSlugField(populate_from="Plaka", unique=True, always_update=True)
    
    def __str__(self):
        return self.Plaka
    
    


