from django.shortcuts import render
from .models import services

# Create your views here.

def servicios(request):
    servicios = services.objects.all()
    return render(request, "services/servicios.html", {'services':servicios})
