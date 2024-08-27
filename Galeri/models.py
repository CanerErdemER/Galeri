from django.db import models
from django import forms
# Create your models here.

class ArabalarModeli(models.Model):

    Marka_Model=models.CharField(max_length=50)
    Fiyat=models.IntegerField()
    Plaka=models.CharField(max_length=20)


