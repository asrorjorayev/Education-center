from .models import Fanlar
from django.shortcuts import render

def categoriya(request):

    return {"categoriya":Fanlar.objects.all()}